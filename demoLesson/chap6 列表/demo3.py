# Author : John
# @Time     : 2021/1/12 15:21
# @Author   : John
# @File     : demo3
# @Software : PyCharm
# 获取指定元素的索引
"""
列表的查询操作
    获取列表中指定元素的索引
    index()->如果列表中存在N个相同元素，只返回相同元素中的第一个元素的索引
            如果查询的元素在列表中不存在，则会抛出ValueError
            还可以在指定的start和stop之间进行查找
    获取列表中的单个元素
    获取单个元素->正向索引从0到N-1 举例lst[0]
                逆向索引从-N到-1 举例lst[-N]
                指定索引不存在，抛出IndexError
"""
lst=['hello','world',98,'hello']
print(lst.index("hello"))