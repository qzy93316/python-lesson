# Author : John
# @Time     : 2021/1/7 18:00
# @Author   : John
# @File     : demo8
# @Software : PyCharm

"""
流程控制语句continue
    用于结束当前循环，进入下一次循环，通常与分支结构中的if一起使用
TODO:要求输出1到50之间所有5的倍数 5，10，15，20，25...
    5的倍数的共同点: 和5的余数为0的数都是5的倍数
    要求使用continue实现
"""

for item in range(1,51):
    if item%5==0:
        print(item)

print('-----------使用continue--------------')
for item in range(1,51):
    if item%5!=0:
        continue
    print(item)