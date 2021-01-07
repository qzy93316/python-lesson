# Author : John
# @Time     : 2021/1/7 16:52
# @Author   : John
# @File     : demo4
# @Software : PyCharm

# 计算1到100之间的偶数和
"""初始化变量"""
a=1
sum=0
"""条件判断"""
while a<100:
    """条件执行体（求和）"""
    if not bool(a%2): #0的bool值为False
        sum+=a
    """改变变量"""
    a+=1
print('1到100之间的偶数和:',sum)