# Author : John
# @Time     : 2021/1/21 15:44
# @Author   : John
# @File     : demo3
# @Software : PyCharm

'''
集合间的关系
    两个集合是否相等
        可以使用运算符==或!=进行判断
    一个集合是否是另一个集合的子集
        可以调用方法issubset进行判断
        B是A的子集
    一个集合是否是另一个集合的超集
        可以调用方法issuperset进行判断
        A是B的超集
    两个集合是否没有交集
        可以调用方法isdisjoint进行判断
'''

s1={10,20,30,40}
s2={30,40,20,10}
print(s1==s2) #True
print(s1!=s2) #False
#一个集合是否是另一个集合的子集
s1={10,20,30,40,50,60}
s2={10,20,30,40}
s3={10,20,90}
print(s2.issubset(s1)) #True
print(s3.issubset(s2)) #False
#一个集合是否是另一个集合的超集
print(s1.issuperset(s2)) #True
print(s1.issuperset(s3)) #False
#两个集合是否没有交集
print(s2.isdisjoint(s3)) #False
s4={100,200,300}
print(s2.isdisjoint(s4)) #True
