# Author : John
# @Time     : 2021/1/19 18:14
# @Author   : John
# @File     : demo2
# @Software : PyCharm

"""
元组的创建方式
    直接小括号
        t=('Python','hello',98)
    使用内置函数tuple()
        t=tuple(('Python','hello',98))
    只包含一个元素的元组需要使用逗号和小括号
        t=(10,)
"""

'''第一种创建方式 使用()'''
t=('Python','hello',98)
print(t)
print(type(t))

t2='Python','hello',98 #省略了小括号
print(t2)
print(type(t2))

t3=('Python',) #只包含一个元素的元组需要使用逗号和小括号
print(type(t3))
'''第二种创建方式 使用内置函数tuple()'''
t1=tuple(('Python','hello',98))
print(t1)
print(type(t1))

'''空列表、空字典、空元组的创建方式'''
lst=[]
lst1=list()

d={}
d1=dict()

t4=()
t5=tuple()

print('空列表',lst,lst1)
print('空字典',d,d1)
print('空元组',t4,t5)