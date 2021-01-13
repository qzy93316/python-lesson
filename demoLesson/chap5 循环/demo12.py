# Author : John
# @Time     : 2021/1/12 14:49
# @Author   : John
# @File     : demo12
# @Software : PyCharm

# 二重循环中的break和continue
"""二重循环中的break和continue用于控制本层循环"""
for i in range(5): #代表外层循环要执行5次
    for j in range(1,11):
        if j%2==0:
            #break #退出内层循环，不影响外层循环
            continue
        print(j,end="\t")
    print()
