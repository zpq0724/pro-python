# coding=utf-8
"""
python 中标识符由 字母、数字、下划线组成，但不能以数字开头；所有标识符是区分大小写的；
以单下划线开头 _foo 的代表不能直接访问的类属性，需要通过类提供的接口进行访问，不能用 from XXX import * 而导入；
以双下划线__foo代表类的私有成员，以双下划线头和结尾的 __foo__ 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。
可以同一行显示多条语句，方法是用分号分开；如：print ('hello');print ('runoob');
"""
print('hello world')

'''
python 的代码块不适用大括号 {} 来控制类、函数以及其他判断逻辑。python 最具特色的就是用缩进来写模块；
缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，必须严格执行。
'''


if True:
    print ('answer')
    print ('true')
else:
    print ('false')


# python 中以新行作为语句的结束符；也可使用斜杠（\）将一行的语句分为多行显示；如下：
    total = item_one + \
            item_two + \
            item_three
# 语句中包含 [], {}, 或 () 括号就不需要使用多行连接符；如下实列：
    days = ['Monday', 'Tuesday', 'Wednesday'
            'Thursday', 'Friday']

# python 可以使用（‘），（“）， 三引号（’‘’ 或 ”“”）表示字符串，引号的开始与结束必须是相同类型的；
# 其中三引号可以由多行组成，常用于文档字符串，被当做注释；


#python 多行注释
'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''
