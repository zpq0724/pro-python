list = ['a', 'b', 'c', 'd']
print(list)


# del () 方法可以删除列表中的元素
del list[3]
print(list)


# append() 方法可以向列表末尾添加一个元素
item = {'name' : 'zpq'}
list.append(item)
print(list)

# list.count(obj) 统计某个元素在列表中出现的次数
aList = [123, 'xyz', 'zara', 'abc', 123]
print ("Count for 123 : ", aList.count(123))

# pop() 方法可以删除列表末尾的元素
list = ['a', 'b', 'c', 'd']
delItem = list.pop()
print(delItem)


# len() 方法可以返回列表的长度

# [1, 2, 3] + [4, 5, 6] 组合
print([1, 2, 3] + [4, 5, 6])


# 3 in [1, 2, 3] 判断 3 是否在列表中
print(3 in [1, 2, 3])

# 迭代
for x in [1, 2, 3]: 
  print (x)