# Author : John
# @Time     : 2021/1/13 14:19
# @Author   : John
# @File     : demo3
# @Software : PyCharm

"""
字典中元素的获取
    []          -> scores['张三']
    get()方法    -> scores.get['张三']
[]取值与使用get()取值的区别
    []如果字典中不存在指定的key,抛出keyError异常
    get()方法取值，如果字典中不存在指定的key，并不会抛出keyError而是返回None,可以通过参数设置默认的value,以便指定的key不存在时返回
"""
scores={'张三':100,'李四':98,'王五':45}
print(scores['张三'])
# print(scores['陈六']) #KeyError: '陈六'

print(scores.get('张三'))
print(scores.get('陈六')) #None
