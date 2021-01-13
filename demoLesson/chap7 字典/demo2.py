# Author : John
# @Time     : 2021/1/13 14:11
# @Author   : John
# @File     : demo2
# @Software : PyCharm

# 字典的创建
"""
最常用的方式: 使用花括号 -> scores={ '张三': 100, '李四': 98, '王五'： 45 }
使用内置函数dict() -> dict(name='jack',age=20)
"""

# 使用{}创建字典
scores={'张三':100,'李四':98,'王五':45}
print(scores)
print(type(scores))

# 第二种创建dict()
student=dict(name='jack',age=20)
print(student)

# 空字典
d={}
print(d)