# Author : John
# @Time     : 2021/1/6 18:07
# @Author   : John
# @File     : demo4
# @Software : PyCharm

# 分支结构_双分支结构
'''
双分支结构if...else,二选一执行
    if 条件表达式 :
        条件执行体1
    else:
        条件执行体2
'''

#从键盘录入一个整数，编写程序让计算机判断是奇数还是偶数
num=int(input('请输入一个整数'))

#条件判断
if num%2==0 :
    print(num,'是偶数')
else :
    print(num,'是奇数')
