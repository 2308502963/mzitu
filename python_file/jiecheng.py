# -*- coding: cp936 -*-
#  ��n�Ľ׳�  �������
def jiecheng():
    print ("����n��")
    sum=1
    n=eval(input(""))
    while n<=1:
        print("��������n��Ҫ��n����1��:")
        n=eval(input(""))
    while n>1:
        sum=sum*n
        n=n-1
    return sum
s=jiecheng()
print(s)
