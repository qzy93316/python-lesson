# Author : John
# @Time     : 2021/1/12 15:33
# @Author   : John
# @File     : demo4
# @Software : PyCharm

# 获取列表中的多个元素
"""
语法格式
    列表名[start:stop:step]
切片操作
    切片结果：原列表片段的拷贝
    切片的范围：[start,stop)
    step默认为1：简写为[start,stop]
    step为正数:[:stop:step]->切片的第一个元素默认是列表的第一个元素
              [start::step]->切片的最后一个元素默认是列表的最后一个元素     从start开始往后计算切片
    step为复数：[:stop:step]->切片的第一个元素默认是列表的最后一个元素
               [start::step]->切片的最后一个元素默认是列表的第一个元素      从start开始往前计算切片
"""
lst=[10,20,30,40,50,60,70,80]
#start=1,stop=6,step=1
print('原列表',id(lst))
lst2=lst[1:6:1]
print('切的片段',id(lst2))
print(lst[1:6]) #默认步长为1
print(lst[1:6:])
#start采用默认,stop=6,step=2
print(lst[:6:2])
#start=1,step=2,stop采用默认
print(lst[1::2])
print('------------step步长为负数-------------------------')
print('原列表',lst)
print(lst[::-1])
#start=7,stop省略,step=-1
print(lst[7::-1])
print(lst[6:0:-2])

