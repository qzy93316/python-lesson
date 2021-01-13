# Author : John
# @Time     : 2021/1/12 16:57
# @Author   : John
# @File     : demo9
# @Software : PyCharm

# 列表元素的排序操作
"""
常见的两种方式
    调用sort()方式，列表中的所有元素默认按照从小到大的顺序进行排序，可以指定reverse=True,进行降序排序
    调用内置函数sorted(),可以指定reverse=True,进行降序排序，原列表不发生改变
"""
lst=[20,40,10,98,45]
print('排序前的列表',lst,id(lst))
#开始排序，调用列表对象的sort方法，升序排序
lst.sort()
print('排序后的列表',lst,id(lst))

#通过指定关键字参数，将列表中的元素进行降序排序
lst.sort(reverse=True) #reverse=True 表示降序排序,reverse=False就是升序排序
print(lst)
lst.sort(reverse=False)
print(lst)

print('------------------------------使用内置函数sorted()对列表进行排序，将产生一个新的列表对象---------------------------------------')
lst=[20,40,10,98,54]
print('原列表',lst)
#开始排序
new_list=sorted(lst)
print(lst)
print(new_list)
#指定关键字参数，实现列表元素的降序排序
desc_list=sorted(lst,reverse=True)
print(desc_list)