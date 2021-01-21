# Author : John
# @Time     : 2021/1/21 15:13
# @Author   : John
# @File     : demo2
# @Software : PyCharm
'''
集合的相关操作
    集合元素的判断操作
        in 或 not in
    集合元素的新增操作
        调用add()方法，一次添加一个元素
        调用update()方法,一次至少添加一个元素
    集合元素的删除操作
        调用remove()方法，一次删除一个指定元素，如果指定的元素不存在抛出KeyError
        调用discard()方法，一次删除一个指定元素，如果指定的元素不存在不抛异常
        调用pop()方法，一次只删除一个任意元素
        调用clear()方法，清空集合
'''
s={10,20,30,405,60}
#集合元素的判断操作
print(10 in s) #True
print(100 in s) #False
print(10 not in s) #False
print(100 not in s) #True
#集合元素的新增操作
s.add(80)
print(s)
s.update({200,400,300})
print(s)
s.update({100,99,8})
s.update((78,64,56))
print(s)
#集合元素的删除操作
s.remove(100)
print(s)
# s.remove(500) KeyError: 500
s.discard(500)
print(s)
s.pop()
s.pop()
# s.pop(400) #TypeError: pop() takes no arguments (1 given)
print(s)

s.clear()
print(s)
