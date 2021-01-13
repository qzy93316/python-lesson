# Author : John
# @Time     : 2021/1/13 15:06
# @Author   : John
# @File     : demo8
# @Software : PyCharm

# 字典生成式
"""
内置函数zip()
用于将可迭代的对象作为参数，将对象中对应的元素打包成一个元组，然后返回由这些元组组成的列表
"""
items=['Fruits','Books','Others']
prices=[96,78,85]

d={ item.upper():price for item,price in zip(items,prices) }
print(d)