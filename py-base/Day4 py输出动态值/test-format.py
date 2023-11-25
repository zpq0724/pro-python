name = "zpq"
age = "18"
#  3.6 及以上版本支持 f-string 来格式化字符串
print(f"my name is {name}, I am {age} years old")

print("my name is {}, I am {} years old" .format(name, age))



'''
  Python 中文编码
  Python 中默认的编码格式是 ASCII 格式，没有修改编码格式时无法正确打印汉字
  在文件开头加 # coding=utf-8
  Python3.x 源码文件默认使用 uef-8 编码，所以可以正常解析中文，无需指定UTF-8编码
'''
print('hello world')

print('你好，世界')