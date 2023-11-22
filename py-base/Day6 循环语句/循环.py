# coding=utf-8
'''
  break 语句:	
    在语句块执行过程中终止循环，并且跳出整个循环
    
  continue 语句:	
    在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环
    
  pass 语句:	
    什么都不做，pass是空语句，是为了保持程序结构的完整性。

'''



'''
  1. for 循环可以遍历任何序列中的项目，如一个列表或者一个字符串
  2. TODO for 循环
  
'''




'''
  2 while 循环
  
'''
count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")



# break、continue 语句
for letter in 'Python':     # 第一个实例
   if letter == 'h':
      break
   print ('当前字母 :', letter)
   
   
   
# pass 语句,
for letter in 'Python':
   if letter == 'h':
      pass
      print ('这是 pass 块')
   print ('当前字母 :', letter)
 
print ("Good bye!")


'''
下面的 pass 便是占据一个位置，因为如果定义一个空函数程序会报错，
当你没有想好函数的内容是可以用 pass 填充，使程序可以正常运行。
'''
def sample(n_samples):
  pass