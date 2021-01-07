# Author : John
# @Time     : 2021/1/7 16:44
# @Author   : John
# @File     : demo3
# @Software : PyCharm

#  四步循环法
"""
    1.初始化变量
    2.条件判断
    3.条件执行体(循环体)
    4.改变变量
    总结： 初始化变量与条件判断的变量与改变的变量为同一个
"""

a=0
sum=0 #用于存储累加和
while a<5:
    sum+=a
    a+=1
print('和为:',sum)
