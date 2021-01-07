# Author : John
# @Time     : 2021/1/7 16:59
# @Author   : John
# @File     : demo5
# @Software : PyCharm

# for_in循环
"""
for-in循环
    in表达从（字符串、序列等）中取值，又称为遍历
    for-in遍历的对象必须是可迭代对象
for-in的语法结构
    for 自定义的变量 in 可迭代对象

循环体内不需要访问自定义变量，可以将自定义变量替代为下划线
"""
for item in "Python":
    print(item)

#range()产生一个整数序列，也是一个可迭代对象
for i in range(10):
    print(i)

#循环体内不需要访问自定义变量，可以将自定义变量替代为下划线
for _ in range(5):
    print('人生苦短，我用Python')

print('使用for循环，计算1到100之间的偶数和')
sum=0
for item in range(1,101):
    if not bool(item%2): # iif item%2==0
        sum+=item
print('1到100之间的偶数和为:',sum)
