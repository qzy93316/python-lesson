# Author : John
# @Time     : 2021/1/13 14:43
# @Author   : John
# @File     : demo5
# @Software : PyCharm

# 获取字典视图
"""
获取字典试图的三种方法
    keys()      获取字典中所有key
    values()    获取字典中所有value
    items()     获取字典中所有key,value对
"""
scores={'张三':100,'李四':98,'王五':45}
# 获取所有的key
keys=scores.keys()
print(keys)
print(type(keys))
print(list(keys)) #将所有的key组成的视图转成列表
# 获取所有的value
values=scores.values()
print(values)
print(type(values))
print(list(values))
# 获取所有的key-value对
items=scores.items()
print(items)
print(type(items))
print(list(items)) # 转换之后的列表元素是由元组组成