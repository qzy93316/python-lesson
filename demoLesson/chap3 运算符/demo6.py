# Author : John
# @Time     : 2021/1/6 14:00
# @Author   : John
# @File     : demo6.py
# @Software : PyCharm

# 运算符_布尔运算符
a,b=1,2
print('---------------and 并且---------------------')
print(a==1 and b==2)
print(a==1 and b<2)
print(a!=1 and b==2)
print(a!=1 and b!=2)

print('---------------or 或者---------------------')
print(a==1 or b==2)
print(a==1 or b<2)
print(a!=1 or b==2)
print(a!=1 or b!=2)

print('---------------not 对bool类型操作数取反---------------------')
f=True
f2=False
print(not f)
print(not f2)

print('---------------in与not in---------------------')
s='helloworld'
print('w' in s)
print('k' in s)
print('w' not in s)
print('k' not in s)
