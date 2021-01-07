# Author : John
# @Time     : 2021/1/7 17:21
# @Author   : John
# @File     : demo6
# @Software : PyCharm

"""
输出100到999之间的水仙花数
举例
153=3*3*3+5*5*5+1*1*1
"""
for item in range(100,1000):
    ge=item%10 #个位
    shi=item//10%10 #十位
    bai=item//100 #百位
    #print(ge,shi,bai)
    if ge**3+shi**3+bai**3==item:
        print(item)