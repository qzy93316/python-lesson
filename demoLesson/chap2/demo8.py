# Author : John
# @Time     : 2021/1/5 17:26
# @Author   : John
# @File     : demo8.py
# @Software : PyCharm

# 类型转换_str()函数与int()函数
name="张三"
age=20
print(type(name),type(age)) # 说明name与age的数据类型不相同
# print('我叫' + name + '今年,' + age + '岁') #当将str类型与int类型进行拼接时，报错，解决方案，类型转换
print('我叫' + name + '今年,' + str(age) + '岁') # 将int类型通过str()函数转化为了str

print("-------------str()将其他类型转化成str类型----------------")
a=10
b=198.8
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))

print("-------------int()将其他类型转化成int类型----------------")
s1='128'
f1=98.7
s2='76.77'
ff=True
s3='hello'
print(type(s1),type(f1),type(s2),type(ff),type(s3))
print(int(s1),type(int(s1))) # 将str转换为int,字符串为数字串
print(int(f1),type(int(f1))) # float转成int类型，截取整数部分，舍掉小数部分
# print(int(s2),type(int(s2))) # 将str转成int类型，报错，因为字符串为小数串
print(int(ff),type(int(ff)))
# print(int(s3),type(int(s3))) # 将str转成int类型时，字符串必须为数字串（整数），非数字串是不允许的
