# Author : John
# @Time     : 2021/1/12 16:08
# @Author   : John
# @File     : demo5
# @Software : PyCharm

# 列表元素的查询操作
"""
判断指定元素在列表中是否存在
    元素 in 列表名
    元素 not in 列表名
列表元素的遍历
    for 迭代变量 in 列表名:
    操作
"""
print('p' in 'python') #True
print('k' not in 'python') #True

lst=[10,20,'python','hello']
print(10 in lst) #True
print(100 in lst) #False
print(10 not in lst) #False
print(100 not in lst) #True

for item in lst:
    print(item)