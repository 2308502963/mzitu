#判断年龄进网吧
'''
age=eval(input("你今年多大了?"))

if age>=18:
    print("你可以进网吧嗨皮...")
else:
    print("你还没长大,应该回家写作业!")
print("这句话什么时候执行?都会执行")
'''


#定义一个整数变量age，编写代码判断年龄是否正确
'''
age=eval(input("输入一个年龄\n"))

#要求人的年龄在0-120之间

if age>0 and age<120:
    print("年龄正确!")
else:
    print("年龄不正确!")
'''

#定义两个整数变量：python_score、c_score，编写代码判断成绩
'''
python_score=eval(input("输入你的第一门成绩:\n"))
c_score=eval(input("输入你的第二门成绩:\n"))

#要求只要有一门成绩>60分就算合格
if python_score>60 or c_score>60:
    print("考试通过!")
else:
    print("考试失败!")
'''

#定义一个布尔型变量‘is_employee’，编写代码判断是否是本公司员工
'''
is_employee = False

#如果不是提示不允许入内

if not is_employee:
    print("非公勿内")

else:
    print("可以进去")
'''


#女友的生日
'''
holiday_name=input("今天是什么节日？\n")

if holiday_name=="情人节":
    print("我给你买玫瑰")
    print("我们去看电影")
elif holiday_name=="平安夜":
    print("我们去吃苹果")
    print("我们去吃大餐")
elif holiday_name=="生日":
    print("我给你买蛋糕")
else:
    print("每天都是节日啊....")

'''

#火车站安检


#定义布尔型变量has_ticket表示是否有票
#定义整型变量knife_length表示刀的长度，单位：厘米
#首先检查是否有车票，如果有，才允许案件
#安检时，需要检查刀的长度，判断是否超过20厘米
    #如果超过20厘米，提示刀的长度，不允许上车
    #如果不超过20厘米，安检通过
#如果没有车票，不允许进门
'''
has_ticket=eval(input("有票吗？(True/False)\n"))

if not has_ticket:
    print("大哥，你要先买票啊！")
else:
    knife_length=eval(input("你的刀有多长？"))
    if knife_length>=20:
        print("不允许携带{}厘米的刀上车".format(knife_length))
    else:
        print("安检通过，祝您旅途愉快....")
    
'''


#石头剪刀布

'''
import random
player=int(eval(input("请出拳 石头（1）/剪刀（2）/布（3）：")))

computer=random.randint(1,3)
print(computer)

if(player==1 and computer==2) or (player==2 and computer==3) or (player==3 and computer==1):
    print("电脑弱爆了")
elif player==computer:
    print("心有灵犀")
else:
    print("你输了")
'''



#在控制台打印小星星，每一行星星的数量一次递增
'''
for i in range(5):
    print("*"*i)
print("*",end="")
'''
'''
for i in range(5):
    row=1
    while row<=i:
        print("*",end="")
        row+=1
    print("")
'''


#打印九九乘法表
'''
print("{:^}".format("九九乘法表"))
for i in range(10):
    row=1
    while row<=i:
        print("{}*{}={}\t".format(row,i,row*i),end="")
        row+=1
    print("")
'''

#判断是否是素数


import math

a = int(input("输入一个数："))
for i in range(2,a-1):
    if(a%i==0):
        print("不是素数")
        break
else:
    print("是素数")













