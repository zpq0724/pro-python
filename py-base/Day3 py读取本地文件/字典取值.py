'''
  1. 统计元素个数
'''
dict = {}
list = ['Y', 'Y', 'Y','Y', 's', 's', 's']

for i in list:
  dict[i] = dict.get(i, 0)  + 1
  print(i)
  print(dict[i])
  # print(dict1)
print(dict)



"""
  2. 字典中取值
"""
dict1 = {'name': 'zpq'}
# get() 的键在字典中不存在时，会返回 None 或 指定内容
print(dict1.get('name'))
print(dict1.get('age', 18))

# dict[key] 的键在字典中不存在时，会报错 KeyError: key
print(dict1['name'])

# 字典中嵌套取值
dict2 = {'key1': 'value1', 'key2': {'key3': 'value3'}}
print(dict2.get('key2').get('key3'))