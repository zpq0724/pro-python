demo 文档：
    https://www.byhy.net/tut/webdev/django/11/


demo 视频：
    https://www.bilibili.com/video/BV1AE41117Up?p=32&spm_id_from=pageDriver&vd_source=e1a8b853ea61db45ea22bdb6ffe4c748



基本命令：
1. 启动项目：
    python manage.py runserver

2. 创建应用（app) :
    python manage.py startapp name


re_path(r'^', include(‘common_models.urls’))

  r'^' 是一个空的正则表达式，它会匹配任何 URL，因此它会优先匹配到第一个定义的路径。




尝试使用 sql 创建：
  Django 中 对数据库表的操作， 应该都通过 Model对象 实现对数据的读写，而不是通过SQL语句。
