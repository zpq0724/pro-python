dict = {'a': 1, 'b': 2, 'b': '3'}
print(type(dict))
print(dict['a'])


# 删除键是 'b' 的条目
dict.pop('b')
print(dict)


# 清空字典
dict.clear()
print(dict)


# len() 函数计算字典元素个数
dict = {'a': 1, 'b': 2, 'c': '3'}
print(len(dict))


# copy() 函数返回一个字典的浅复制
dict1 = {'a': 1, 'b': 2, 'c': '3'}
dict2 = dict1.copy()
dict2['a'] = 100
print(dict2)


# items() 函数以列表返回可遍历的(键, 值) 元组数组
dict = {'a': 1, 'b': 2, 'c': '3'}
print(dict.items())

tinydict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
for key in  tinydict:
    print (tinydict[key])
    
    
tinydict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
for key, value in  tinydict.items():
    print (key, value)
    
    
# dict.keys() 函数以列表返回一个字典所有的键
dict = {'a': 1, 'b': 2, 'c': '3'}
_keys = dict.keys()
print(_keys)



# 把字典dict2的键/值对更新到dict里
tinydict = {'Name': 'Zara', 'Age': 7}
tinydict2 = {'Sex': 'female' }

tinydict.update(tinydict2)
print(tinydict)