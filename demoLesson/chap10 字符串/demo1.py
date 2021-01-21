# Author : John
# @Time     : 2021/1/21 17:39
# @Author   : John
# @File     : demo1
# @Software : PyCharm

'''
字符串的驻留机制
    字符串：在python中字符串是基本数据类型，是一个不可变的字符序列
什么叫字符串的驻留机制呢？
仅保存一份相同且不可变字符串的方法，不同的值被存放在字符串的驻留池中，Python的驻留机制对相同的字符串只保留一份拷贝，
后续创建相同字符串时，不会开辟新空间，而是把该字符串的地址赋给新创建的变量
'''

a='python'
b="python"
c='''python'''
print(a,id(a))
print(b,id(b))
print(c,id(c))

# 详细驻留机制见oneNote-Python-字符串的驻留机制
