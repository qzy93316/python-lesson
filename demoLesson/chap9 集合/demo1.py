# Author : John
# @Time     : 2021/1/21 14:48
# @Author   : John
# @File     : demo1
# @Software : PyCharm

'''
什么是集合
    Python语言提供的内置数据结构
    与列表、字典一样都属于可变类型的序列
    集合是没有value的字典
集合的创建方式
    直接{}
        s={'Python','hello',98}
    使用内置函数set()
'''

# 第一种创建方式使用{}
s={2,3,4,5,5,6,7,7} #集合中的元素不允许重复
print(s)

# 第二种创建方式使用set()
s1=set(range(6))
print(s1,type(s1))

s2=set([1,2,4,5,5,5,6,6])
print(s2,type(s2))

s3=set((1,2,4,5,6,6,65)) # 集合中的元素是无序的
print(s3,type(s3))

s4=set('Python')
print(s4,type(s4))

s5=set({12,4,34,55,66,44,4})
print(s5,type(s5))

# 定义一个空集合
s6={} #dict字典类型
print(type(s6))

s7=set()
print(type(s7))