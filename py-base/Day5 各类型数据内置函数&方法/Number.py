'''
  python Number 数据类型用于存储数值
  数据类型是不允许改变的。如果改变 Number 数据类型的值，将重新分配内存空间。
  
  支持四种不同的数值类型：
    整型（int）：
    长整型（long）： 1L
    浮点型（float）： 1.0
    复数（complex）： 1j
    
    
  python 中数学运算常用的函数基本在 math 模块、cmath 模块(复数运算的函数)中：
     math 模块: 提供了很多对浮点数的数学运算函数
     cmath 模块： 提供复数运算的函数
     要使用 math 模块和 cmath 模块，必须先导入模块:
      import math
      import cmath
      
    dir(math) 查看 math 模块中的所有函数
  

'''
num1 = 1
num2 = 2
num3 = 3
print(num1, num2, num3)

# 删除单个或多个变量
del num1, num2

print( num3)


str1 = '1'
print(int(str1))
num2 = 2
print(str(num2), type(str(num2)))


# python 数学函数
print(abs(-10))
