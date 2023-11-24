'''
  1. 下面两行代码中导入的 PgSqlDAO 等的作用是什么？
    from process_biz.app.dao.TblMhp import TblAssetPushPolicy, TblAssetPushData
    from process_biz.app.dao.pgsqldao import PgSqlDAO

    问题答案：见 根目录中 base_faq.txt 中 10、11 条！！！

  2. agent_task.py 文件 定时任务和周期任务，执行？
    def main():
      pass
    
    if __name__ == '__main__':
      main()

'''


import traceback
import re
from flask import request
import HIHTTP
from process_biz.app.dao.pgsqldao import PgSqlDAO
from process_biz.app.dao.TblMhp import TblAssetPushPolicy

class IAssetPushPolicy(HIHTTP.Resource):
  '''
    资产信息转发配置
  '''
  def check_req_params(self, request_json):
    '''
      检查请求参数合法性
    '''
    all_sync_period = request_json.get('all_sync_period')
    add_sync_period = request_json.get('add_sync_period')
    all_sync = request_json.get('all_sync', 0)
    add_sync = request_json.get('add_sync', 0)
    assert all_sync or add_sync, '请指定同步方式'
    push_mode = request_json.get('push_mode', 0)
    address = request_json.get('address', '')
    assert address, '服务器地址不能为空'
    # 需要支持 https://10.66.23.177:3000 形式的服务器地址
    assert re.match(r'^https?:/{2}\w.+$', address), u'服务器地址不合法'
    # 全量模式 增量模式 推送方式 是否合法
    assert all_sync in [0, 1] and add_sync in [0, 1] and push_mode in [0, 1], '模式配置有误'
    # 全量增量同步周期 单位秒，5分钟
    if all_sync_period:
      assert 300 <= all_sync_period <= 43200, '全量同步周期不小于5分钟，不大于720分钟'
    # 批量推送上限 batch_limit 必须大于1，小于1000，单个为1
    if request_json.get('batch_limit'):
      if push_mode:
        assert request_json.get('batch_limit') > 1 and request_json.get('batch_limit') < 500, '批量推送上限不小于1，不大于500'
      else:
        assert request_json.get('batch_limit') == 1, '单个推送模式，推送上限为1'


  def post(self):
    """
      新建资产推送配置
    """
    # 创建一个 PgSqlDAO 对象,可使用 PgSqlDAO 类提供的方法方位 PostgreSQL 数据库
    pgsql = PgSqlDAO()
    # session 适用于增,删,改,需要手动处理事务的提交.
    ses = pgsql.session
    try:
      request_json = request.get_json()
      HIHTTP.restloger.debug("request_json: %s" % request_json)
      self.check_req_params(request_json)
      policy_name = request_json.get('policy_name')
      '''
        ses.query() 使用会话对象 ses 创建一个查询对象，用于执行 TblAssetPushPolicy 表的查询.
        .filter() 是对查询对象应用的过滤条件。其中 TblAssetPushPolicy.policy_name 是表中的一个列名，policy_name 是一个变量，用于指定希望匹配的值。
          这个过滤条件可以根据需要进行调整，以限制查询结果。
        .first() 是执行查询，返回结果的第一条记录。如果没有匹配的记录，则返回 None。
      '''
      obj = ses.query(TblAssetPushPolicy).filter(
        TblAssetPushPolicy.policy_name == policy_name).first()
      assert not obj, '您输入的配置名称已存在'
      push_mode = request_json.get('push_mode', 0)
      if push_mode:
        batch_limit = request_json.get('batch_limit', 50)
      else:
        batch_limit = 1
      policy_data = {
        'policy_name': request_json.get('policy_name'),
        'address': request_json.get('adress'),
        'all_sync': request_json.get('all_sync', 0),
        'add_sync': request_json.get('add_sync', 0),
        'batch_limit': batch_limit
      }
      # 表中插入数据
      TblAssetPushPolicy.insert(policy_data)
      # 判断是否插入成功
      inster_result = ses.query(TblAssetPushPolicy).filter(TblAssetPushPolicy.policy_name == policy_name).first()
      assert inster_result, '配置创建异常'
      return {'errCode': 0, 'errMsg': "Success", 'id': obj.id}
    except Exception as e:
      return {'errCode': 1, 'errMsg': e.args[0] if e.args[0] else "请求参数格式有误"}
    finally:
      # 关闭创建的数据库会话对象ses, 释放与数据库的连接和资源。避免资源泄漏或其他潜在问题
      # finally 关键字，无论是否发生异常，都会执行。
      ses.close()


def get(self, request):
  '''
    获取资产推送配置
  '''

  # 创建访问数据库的会话对象， 
  # sessionq, 自动提交事务的session, 适用于查询、自动提交事务
  pgsql = PgSqlDAO()
  ses = pgsql.sessionq

  try:
    data = dict()
    req_json = request.args
    size = int(req_json.get('size', 10))
    page = int(req_json.get('page', 1))
    keyword = req_json.get('keyword', '')

    if size > 0 and page > 0:
      data['page'] = page
      data['size'] = size
      data['totalSize'] = 0
      '''
        .filter() 方法是对查询对象应用过滤条件。
          其中使用了 TblAssetPushPolicy.policy_name.ilike("%" + keyword.replace('_', '\\_') + "%") 来筛选符合条件的记录。
          这个过滤条件使用 ilike 来进行不区分大小写的模糊匹配，"%keyword%" 表示在 policy_name 字段中包含指定关键字的记录。

        .order_by() 方法是对查询结果进行排序。
          其中使用了 TblAssetPushPolicy.id.desc() 来对 id 列进行降序排序。

        .limit() 方法是对查询结果进行限制。最多返回 size 条记录。

        .offset() 方法是对查询结果进行分页操作,确定从查询结果中的哪个位置开始获取记录
          其中使用了 (page - 1) * size 来计算偏移量。

        .all() 执行查询，并将查询结果作为列表返回给变量 result。
      '''
      result = ses.query(TblAssetPushPolicy).filter(
        TblAssetPushPolicy.policy_name.ilike(
          "%"+keyword.replace('_', '\\_')+'%'
        )
      ).order_by(TblAssetPushPolicy.id.desc()).limit(size).offset((page -1) * size).all()


      '''
        .count() 方法是对查询结果执行计数操作，返回符合条件的记录数量
      '''
      count = ses.query(TblAssetPushPolicy).filter(
        TblAssetPushPolicy.policy_name.ilike("%" + keyword.replace('_', '\\_') + "%")).count()
      
      if count:
        data['totalSize'] = count
      
      data['newList'] = []
      for item in result:
        data_row = dict()
        data_row['id'] = item.id
        data_row['policy_name'] = item.policy_name
        data_row['address'] = item.address
        data_row['all_sync'] = item.all_sync
        data_row['add_sync'] = item.add_sync
        data_row['batch_limit'] = item.batch_limit
        data['newList'].append(data_row)

      # for item in result:
      #   data['newList'].append({
      #     'id': item.id,
      #     'policy_name': item.policy_name,
      #     'address': item.address,
      #     'all_sync': item.all_sync,
      #     'add_sync': item.add_sync,
      #     'batch_limit': item.batch_limit
      #   })
      response_data = {
        'errCode': 0,
        'errMsg': "Success",
        'data': data
      }
      return response_data, HIHTTP.HTTPCODE.OK
    else:
      response_data = {"errCode": 1, "errMsg": '数据不合法'}

  except Exception as e:
    return {'errCode': 1, 'errMsg': e.args[0] if e.args[0] else "请求参数格式有误"}
  
  finally:
    ses.close()
  