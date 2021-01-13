# Author : John
# @Time     : 2021/1/13 14:34
# @Author   : John
# @File     : demo4
# @Software : PyCharm

# 字典元素的增删改操作
"""key的判断"""
scores={'张三':100,'李四':98,'王五':45}
print('张三' in scores)
print('张三' not in scores)

# 删除指定的键值对key-value
del scores['张三']
print(scores)

# 清空字典的元素
scores.clear()
print(scores)

# 新增元素
scores['陈六']=98
print(scores)

# 修改元素
scores['陈六']=100
print(scores)

