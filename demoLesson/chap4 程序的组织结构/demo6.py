# Author : John
# @Time     : 2021/1/7 11:44
# @Author   : John
# @File     : demo6.py
# @Software : PyCharm

#   分支结构_嵌套if
"""
    语法结构：
    if 条件表达式1:
        if 内层条件表达式：
            内层条件执行体1
        else:
            内层条件执行体2
    else 条件执行体

    会员 >= 200 8折
        >= 100 9折
        不打折
    非会员 >=200 9.5折
        不打折
"""

answer=input('您是会员吗?y/n')
money=float(input('请输入您的购物金额'))
#外层判断是否是会员
if answer == 'y': #会员
    if money >= 200:
        print('付款金额为:',money*0.8,'元')
    elif 100 <= money <200:
        print('付款金额为:',money*0.9,'元')
    else:
        print('付款金额为:',money,'元')
else: #非会员
    if money >= 200:
        print('付款金额为:',money*0.95,'元')
    else:
        print('付款金额为:',money,'元')
