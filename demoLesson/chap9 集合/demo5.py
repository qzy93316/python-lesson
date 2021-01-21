# Author : John
# @Time     : 2021/1/21 16:30
# @Author   : John
# @File     : demo5
# @Software : PyCharm

'''
集合生成式
用于生成集合的公式
    { 表示集合元素的表达式 for 自定义变量 in 可迭代对象 }
    将{}修改为[]就是列表生成式
    没有元组生成式
'''
# 列表生成式
lst=[ i*i for i in range(6)]
print(lst)

# 集合生成式
s={ i*i for i in range(10)}
print(s)



