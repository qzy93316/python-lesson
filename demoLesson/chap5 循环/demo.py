# Author : John
# @Time     : 2021/1/7 12:50
# @Author   : John
# @File     : demo
# @Software : PyCharm

# range函数的使用
"""
 range()函数
    用于生成一个整数序列
    创建range对象的三种方式
        1.range(stop)->创建一个(0,stop)之间的整数序列，步长为1
        2.range(start,stop)->创建一个(start,stop)之间的整数序列，步长为1
        3.range(start,stop,step)->创建一个(start,stop)之间的整数序列，步长为step
    返回值是一个迭代器对象
    range类型的优点:不管range对象表示的整数序列有多长，所有range对象占用的内存空间都是相同的，因为仅仅需要存储start,stop,step,只有当用到range对象时，才会去计算
 序列中的相关元素
    in与not in 判断整数序列中是否存在(不存在)指定整数
"""
r=range(10) #[0,1,2,3,4,5,6,7,8,9],默认从0开始，默认相差1称为步长
print(r) #range(0,10)
print(list(r)) #用于查看range对象中的整数序列 ->list是列表的意思

r=range(1,10) #指定了初始值，从1开始，到10结束（不包含10）,默认步长为1
print(list(r)) #[1,2,3,4,5,6,7,8,9]

r=range(1,10,2)
print(list(r)) #[1,3,5,7,9]

# 判断指定的整数  在序列中是否存在 in,not in
print(10 in r) #False 10不在当前的r这个整数序列中
print(9 in r)
print(10 not in r)

    
