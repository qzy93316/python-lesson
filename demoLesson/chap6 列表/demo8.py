# Author : John
# @Time     : 2021/1/12 16:50
# @Author   : John
# @File     : demo8
# @Software : PyCharm

# 列表元素的修改操作
"""
为指定索引的元素赋予一个新值
为指定的切片赋予一个新值
"""
lst=[10,20,30,40]
#一次修改一个值
lst[2]=100
print(lst)
lst[1:3]=[300,400,500,600]
print(lst)