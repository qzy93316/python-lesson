# Author : John
# @Time     : 2021/1/6 17:47
# @Author   : John
# @File     : demo3
# @Software : PyCharm

# 分支结构_单分支结构
'''
    if 条件表达式 ：
        条件执行体
'''
money=1000 #余额
s=int(input('请输入取款金额')) #取款金额
# 判断余额是否充足
if money>=s:
    money-=s
    print('取款成功,余额为',money)


