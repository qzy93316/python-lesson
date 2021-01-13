# Author : John
# @Time     : 2021/1/12 16:31
# @Author   : John
# @File     : demo7
# @Software : PyCharm

# 列表元素的删除操作
"""
    方法          操作描述
    remove()    一次删除一个元素
                重复元素只删除第一个
                元素不存在抛出ValueError
    pop()       删除一个指定索引上的元素
                指定索引不存在抛出IndexError
                不指定索引，删除列表中的最后一个元素
    切片         一次至少删除一个元素
    clear()     清空列表
    del         删除列表
"""
lst=[10,20,30,40,50,60,30]
lst.remove(30)
print(lst)
# lst.remove(100) #ValueError: list.remove(x): x not in list

#pop()根据索引移除元素
lst.pop(1)
print(lst)
#lst.pop(5) #IndexError: pop index out of range
lst.pop()
print(lst)

print('--------------切片操作 删除至少一个元素，将产生一个新的列表对象-----------------------')
new_list=lst[1:3]
print('原列表',lst)
print('切片后的列表',new_list)

"""不产生新的列表对象，而是删除原列表中的内容"""
lst[1:3]=[]
print(lst)

"""清除列表中的的所有元素"""
lst.clear()
print(lst)

"""del语句将列表对象删除"""
del lst
print(lst) #NameError: name 'lst' is not defined
