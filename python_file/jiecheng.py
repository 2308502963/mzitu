# -*- coding: cp936 -*-
#  求n的阶乘  函数完成
def jiecheng():
    print ("输入n：")
    sum=1
    n=eval(input(""))
    while n<=1:
        print("重新输入n（要求n大于1）:")
        n=eval(input(""))
    while n>1:
        sum=sum*n
        n=n-1
    return sum
s=jiecheng()
print(s)
