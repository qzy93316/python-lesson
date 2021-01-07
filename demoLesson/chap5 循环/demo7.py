# Author : John
# @Time     : 2021/1/7 17:29
# @Author   : John
# @File     : demo7
# @Software : PyCharm

'''
流程控制语句break
    用于结束循环结构，通常与分支结构if一起使用
TODO:从键盘录入密码，最多录入3次，如果正确就结束循环
'''
# for item in range(3):
#     pwd=input("请输入密码:")
#     if pwd=='8888':
#         print("密码正确")
#         break
#     else:
#         print('密码不正确')
a=0
while a<3:
    pwd=input("请输入密码:")
    if pwd=="8888":
        print("密码正确")
        break
    else:
        print("密码不正确")
    a+=1
