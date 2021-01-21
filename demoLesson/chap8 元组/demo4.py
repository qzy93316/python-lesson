# Author : John
# @Time     : 2021/1/21 14:33
# @Author   : John
# @File     : demo4
# @Software : PyCharm

'''
元组是可迭代对象，所以可以使用for...in进行遍历
t=tuple(('Python','hello',98))
for item in t:
    print(item)
'''

t=('Python','hello',98)
'''第一种获取元组元素的方式，使用索引'''
print(t[0])
print(t[1])
print(t[2])
# print(t[3]) #IndexError: tuple index out of range

'''遍历元组'''
for item in t:
    print(item)