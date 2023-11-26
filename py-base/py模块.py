'''
  用于解释部分 Python 模块的作用
'''

import traceback
'''
  traceback 模块提供了对程序中出现异常时的堆栈跟踪信息进行操作和处理的功能。
  主要作用：
    1. 追踪和记录异常；
    2. 打印堆栈跟踪信息
    3. 异常处理
    4. 格式化异常信息
  
  使用：traceback.format_exc()
'''


'''
  测试代码
'''
a = 9
assert not a , 'a 存在'
print('111')


data = dict()
data['page'] = 1
print(data)



path = 'D:\Coding\A-zpq-project-space\Back-end\python\py-base\Day3 py读取本地文件\json_api-test.json'
try:
    fi = open()
    try:
        fi.read()
    finally:
        fi.close()
        print("最后都会执行")
except FileNotFoundError as e:
    print(f"找不到相应的文件: {e}")
except IOError as e:
    print(f"文件操作失败IOError: {e}")
except Exception as e:
    # 可对比下面两行的输出区别
    # print(f"发生其他异常: {traceback.format_exc()}")
     print(f"发生其他异常: {e}")
finally:
    print("最后会执行finally")
