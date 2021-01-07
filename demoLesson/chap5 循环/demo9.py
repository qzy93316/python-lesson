# Author : John
# @Time     : 2021/1/7 18:09
# @Author   : John
# @File     : demo9
# @Software : PyCharm

"""
    else语句，
    与for..in或while循环结构搭配使用
    循环正常执行没有执行break才会执行else后语句
"""
# for item in range(3):
#     pwd=input("请输入密码:")
#     if pwd=="8888":
#         print("密码正确")
#         break
#     else:
#         print("密码不正确")
#
# else:
#     print("对不起，三次密码均输入错误")
a=0
while a<3:
    pwd = input("请输入密码:")
    if pwd=="8888":
        print("密码正确")
        break
    else:
        print("密码不正确")
    a+=1
else:
    print("对不起，三次密码均输入错误")