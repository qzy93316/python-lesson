# Author : John
# @Time     : 2021/1/21 18:24
# @Author   : John
# @File     : demo3
# @Software : PyCharm

'''
字符串的常用操作
功能          方法名称                    作用
大小写转换      upper()      把字符串中所有字符都转成大写字母
              lower()      把字符串中所有字符都转成小写字母
             swapcase()    把字符串中所有大写字母都转成小写字母，把所有小写字母都转成大写字母
             capitalize()   把第一个字符转换为大写，把其余字符转换为小写
             title()       把每个单词的第一个字符转换为大写，把每个单词的剩余字符转换为小写
'''
s='hello,python'
a=s.upper()
print(s,id(s))
print(a,id(a))
