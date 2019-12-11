'''python七八章例题
'''

'''
try:
    n = eval(input("请输入一个数字:"))
    print("输入的数字的3次方的值:",n**3)
except:
    print("输入错误，请输入一个数字")
'''


'''
try:
    for i in range(5):
        print(10/i,end="")
except:
    print("error")
'''

'''
try:
    print("hahah")
except Exception as e:
    print(Exception,":",e)
else:
    print("no error")
'''

'''
try:
    pass
except Exception as e:
    print("Exception:",e)
finally:
    print("try id done")
'''

'''
a=0
if a==0:
    raise Exception("a must not be zero")
'''

'''
string = "hello python"
for c in string:
    print(c,end="-")
'''

#截取字符串
'''
str="123456一水阿富汗的数据库佛挡杀佛"
print(str[2:10:2])
'''

'''
path="C:\Windows\notepad.exe"
print(path)
'''
'''
path=r"C:\Windows\notepad.exe"
print(path)
'''


#统计字符串中的汉字和标点出现的个数
'''
s="明月几时有？把酒问青天。不知天上宫阙，今昔是何年。我欲乘风归去，又恐琼楼玉宇，高处不胜寒。起舞弄清影，何似在人间？"
n=0    #汉字个数
m=0    #标点个数

liststr=list(s)    #将字符串转化为数组
for i in liststr:  #遍历数组
    if(i.isalpha()):
        n=n+1
    else:
        m=m+1
print("字符数为{},标点符号数为{}".format(n,m))
'''


#计数
from collections import Counter
votes="张力,王志霞,jams,韩梅梅,john,韩梅梅,john,韩梅梅"
namelist=votes.split(",")

print(Counter(namelist))
    
    











