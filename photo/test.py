# _*_ coding: utf-8 _*_
# @Time : 2019/11/17 17:49
# @Author : moran office
# File : test.py
# Software : PyChram
'''
a = "watermelon"; b = "strawberry"; c = "cherry"
if a > b:
     c,a,b = a,b,c
print(a,b,c)'''
'''
x=10
y=20
min = x if x < y else y
print(min)

d = {}
for i in range(26):
    d[chr(i+ord("a"))] = chr((i+13) % 26 + ord("a"))
    for c in "Python":
       print(d.get(c, c), end="")
'''
'''
ls = [1,2,3,4,5,6]
for i in range(len(ls)):
    print(i,end="")
for i in ls:
    print(i,end="")
'''
'''
ss = list(set("jzzszyj")); ss.sort(); print(ss)
print(set("jzzszyj"))
'''
'''
#列表推导式
print([i for i in range(100) if i%13==0])
'''
'''
print(sorted([111, 2, 33], key=lambda x: len(str(x))))
'''
'''
x = {1:2}
x[2]=3
print(x)
'''
'''
x = {'a':'b', 'c':'d'}
print('a' in x)
'''

'''
[3,5,3,7]
#x[len(x):] = [1, 2]
#print(':'.join('abcdefg'.split('cd')))

x = {i:str(i+3) for i in range(3)}
print(''.join(x.values()))

print('Beautiful is better than ugly.'.startswith('Be', 5))

x, y = map(int, ['1', '2'])
print(x+y)

for i in range(1,4):
    for j in range(1,4):
            if (i != j):
                print(i, j, end=',')

f1 = 1
f2 = 1
for i in range(1,5):
    print('{} {} ' .format(f1,f2),end='')
    f1 = f1 + f2
    f2 = f1 + f2

frame = [[1,2,3],[4,5,6],[7,8,9]]
rgb = frame[::-1]
print(rgb)

d = {"zhang":"China", "Jone":"America", "Natan":"Japan"}
for k in d:
    print(k, end="")

ls =list({'shandong':200, 'hebei':300, 'beijing':400})
print(ls)
'''
'''
# 输入三位整数，计算个位、十位和百位的平方和并打印输出
num = eval(input("输入一个三位数:"))
first = num // 100
second = num % 100 // 10
third = num % 10
print(first**2+second**2+third**2)
'''
'''
with open("E:\\scores.txt","r") as fp:
    scores_list_str = fp.read()
    scores_list_str = eval(scores_list_str)
you = 0; liang = 0; zhong = 0;jige = 0; bujige = 0
for i in scores_list_str:
    if i >= 90:
        you = you + 1
    elif 80 <= i < 90:
        liang = liang + 1
    elif 70 <= i < 80:
        zhong = zhong + 1
    elif 60 <= i < 70:
        jige = jige + 1
    else:
        bujige = bujige + 1
scores = {
    "优" : you,
    "良" : liang,
    "中" : zhong,
    "及格" : jige,
    "不及格" : bujige
}
print(scores)
'''