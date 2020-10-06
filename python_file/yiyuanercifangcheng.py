import math
a=eval(input("输入一元二次方程的a系数:"))
b=eval(input("输入一元二次方程的b系数:"))
c=eval(input("输入一元二次方程的c系数:"))
if(b*b-4*a*c<0):
    print("该方程无解!")
else:
    flag=math.sqrt(b*b-4*a*c)
    x1=(-b+flag)/2*a
    x2=(-b-flag)/2*a
    if(x1==x2):
        print("x1=x2=",x1)
    else:
        print("x1=",x1)
        print("x2=",x2)
