# Author : John
# @Time     : 2021/1/12 14:42
# @Author   : John
# @File     : demo11.py
# @Software : PyCharm
"""输出一个99乘法表"""
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"*",j,"=",i*j,end="\t")
    print() #换行