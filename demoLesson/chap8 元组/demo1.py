# Author : John
# @Time     : 2021/1/19 17:45
# @Author   : John
# @File     : demo1
# @Software : PyCharm

# 什么是元组？
"""
Python内置的数据结构之一，是一个不可变序列
不可变序列：字符串，元组：没有增、删、改的操作
可变序列：列表、字典：可以对序列执行增、删、改的操作，对象地址不发生更改

t=('Python','hello',90)
"""
# 可变序列 列表、字典
lst=[10,20,45]
print(id(lst))
lst.append(300)
print(id(lst))
# 不可变序列 字符串、元组
s='hello'
print(id(s))
s=s+'world'
print(id(s))

