# Author : John
# @Time     : 2021/1/21 18:13
# @Author   : John
# @File     : demo2
# @Software : PyCharm

'''
字符串的常用操作
功能          方法名称        作用
查询方法      index()      查找字串substr第一次出现的位置，如果查找的字串不存在时，则抛出ValueError
            rindex()      查找字串substr最后一次出现的位置，如果查找的字串不存在时，则抛出ValueError
             find()       查找字串substr第一次出现的位置，如果查找的字串不存在时，则返回-1
             rfind        查找字串substr最后一次出现的位置，如果查找的字串不存在时，则返回-1
'''

#字符串的查询操作
s='hello,hello'
print(s.index('lo')) #3
print(s.find('lo')) #3
print(s.rindex('lo')) #9
print(s.rfind('lo')) #9

# print(s.index('k')) #ValueError: substring not found
print(s.find('k'))
# print(s.rindex('k')) #ValueError: substring not found
print(s.rfind('k'))