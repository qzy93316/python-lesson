# Author : John
# @Time     : 2021/1/6 13:45
# @Author   : John
# @File     : demo5
# @Software : PyCharm

# 运算符_比较运算符
a,b=10,20
print('a>b吗？',a>b)
print('a<b吗？',a<b)
print('a<=b吗？',a<=b)
print('a>=b吗？',a>=b)
print('a==b吗？',a==b)
print('a!=b吗？',a!=b)
'''一个 = 称为赋值运算符， == 称为比较运算符
一个变量由三个部分组成，标识，类型，值
== 比较的是标识还是值？ 值
比较对象的标识使用 is
'''
a=10
b=10
print(a==b) #True 说明a与b的value相等
print(a is b) #True 说明a与b的id标识，相等
print(id(a))
print(id(b))
lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2) #value -->True
print(lst1 is lst2) #id -->False
print(id(lst1))
print(id(lst2))
print(a is not b) #False a与b的id是相等的
print(lst1 is not lst2)

