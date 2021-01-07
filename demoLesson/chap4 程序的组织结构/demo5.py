# Author : John
# @Time     : 2021/1/7 11:26
# @Author   : John
# @File     : demo5
# @Software : PyCharm

# 分支结构_多分支结构
"""
    语法结构：
    if 条件表达式1 :
        条件执行体1
    elif 条件表达式2 :
        条件执行体2
    elif 条件表达式N :
        条件执行体N
    [else:]
        条件执行体N+1
"""
"""
    从键盘录入一个整数成绩
    90-100 A
    80-89  B
    70-79  C
    60-69  D
    0-59   E
    小于0或大于100为非法数据 
"""
score=int(input('请输入一个成绩:'))
if  90 <= score <= 100:
    print('A级')
elif 80 <= score <= 89:
    print('B级')
elif 70 <= score <= 79:
    print('C级')
elif 60 <= score <= 69:
    print('D级')
elif 0 <= score <= 59:
    print('E级')
else:
    print('对不起，成绩有误，不在成绩的有效范围')
