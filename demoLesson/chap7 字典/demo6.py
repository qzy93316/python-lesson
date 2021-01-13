# Author : John
# @Time     : 2021/1/13 14:51
# @Author   : John
# @File     : demo6
# @Software : PyCharm

# 字典元素的遍历
scores={'张三':100,'李四':98,'王五':45}

for item in scores:
    print(item,scores[item],scores.get(item))