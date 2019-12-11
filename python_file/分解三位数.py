#输入三位整数，分解出个位、十位、百位并输出

num=eval(input("输入一个三位数："))
while(len(str(num))!=3):
    num=eval(input("输入一个三位数："))

 #a表示百位
a=num//100
#b表示十位
b=num%100//10
#c表示个位
c=num%10
print("百位是:{}十位是:{}个位是:{}".format(a,b,c))
