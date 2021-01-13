# Author : John
# @Time     : 2021/1/12 16:13
# @Author   : John
# @File     : demo6
# @Software : PyCharm

# 列表元素的添加操作
"""
    方法     操作描述
 append()   在列表的末尾添加一个元素
 extend()   在列表的末尾至少添加一个元素
 insert()   在列表的任意位置(上)添加一个元素
 切片        在列表的任意位置添加至少一个元素
"""
lst=[10,20,30]
print('添加元素之前',lst,id(lst))
lst.append(100)
print('添加元素之后',lst,id(lst))
lst2=["hello","world"]
#lst.append(lst2) #将lst2作为一个元素添加到列表的末尾
lst.extend(lst2)
print(lst)

#在任意位置上添加一个元素
lst.insert(1,10)
print(lst)

lst3=[True,False,'hello']
#在任意的位置上添加N多个元素
lst[1:]=lst3
print(lst) #[10,True,False,'hello']
