#  [] 通过索引获取字符串中字符
str1 = 'zpq'
print(str1[0])


# [ : ] 截取字符串中的一部分
str2 = 'Hello World!'
print(str2[2:5])


# in 检查是否包含
str3 = 'Hello World!'
print('H' in str3)


# not in 检查是否包含
str4 = 'Hello World!'
print('H' not in str4)


'''
  % 格式化字符串的输出
    %s	 格式化字符串
    %d	 格式化整数
    %f   格式化浮点数字，可指定小数点后的精度
'''
name = 'zpq'
age = 18
print('my name is %a, I am %d years old' % (name, age))