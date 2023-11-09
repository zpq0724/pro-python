# coding=utf-8

'''
  json.dump: 方法，传入一个python对象，将其编码为json格式后存储到IO流中
  json.dumps: 方法，传入一个python对象，将其编码为json格式后存储到str中
  json.load: 方法，传入一个ison格式的文件流，将其解码为python对象
  json.loads: 方法，传入一个json格式的str，将其解码为python对象

  区别：
  dump和dumps是将dict转化成json字符串格式，loads是将json字符串转化成dict格式。
  dump和load也是类似的功能，只是与文件操作结合起来了。

'''


import json

# 1. 写入、读文件
def write_file():

  like_num = input('请输入您喜欢的数字：')

  with open('D:\zpq-private-space\pro-python\Day3\json_api-test.json','w') as fw:

    json.dump(like_num,fw) # 将内容写入文件

  with open('D:\zpq-private-space\pro-python\Day3\json_api-test.json','r') as fr:

    data = json.load(fr) # 读取文件内容

  return data

data = write_file()

print("I know your favorite number! It's {}.".format(data))




# 2.
import json
data = {'key1': 1, 'key2': 2}
print(json.dumps(data)) 
print(json.loads(json.dumps(data)))
print (json.dumps(data) == json.loads(json.dumps(data)))