# coding=utf-8
# https://m.runoob.com/python/python-if-statement.html
a = 1
while a < 7:
    if (a % 2 == 0):
        print(a, "is even")
    else:
        print(a, 'is odd')
    a += 1

# for 循环语句
for letter in 'Python':
    print("当前字母:%s" % letter)


num = 100
print(type(num))

# 浮点类型数据存储不精确；解决方案：导入 decimal 模块；
# str() 将其他类型转成 str 类型；
# int() 将其他类型转成 int 类型， 截取 float 类型的整数部分，舍掉小数部分； boolea 转成 1 或 0；
# float() 将其他类型转成 float 类型；


money = 10000
s = int(input('请输入取款金额'))
if money >= s:
    money = money - s
    print('取款成功， 余额为:', money)
else:
    print('钱不够了')



# pass 语句，什么都不做，用于占位；


# rang() 函数，用于生成一个整数序列。返回值是一个迭代器对象；
# 优点：不管对象表示的整数序列有多长，占用的内存空间都是相同的。 in 与 not in 判断整数序列中是否存在指定的整数。


# 判断数据类型 学习到 37 节