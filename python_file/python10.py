#python第十章
'''
name="小明"

def say_hello():
    print("hello 1")
    print("hello 2")
    print("hello 3")
print(name)

say_hello()
print(name)
'''

#两数求和的函数
'''
def sumtwo(num1,num2):
    sum=num1+num2
    print("%d+%d=%d"%(num1,num2,sum))
sumtwo(1,3)
'''
'''
def sumtwo(num1,num2):
    sum=num1+num2
    return sum
sum=sumtwo(1,3)
print(sum)
'''

'''
i=5

def fun(arg=i):
    print(arg)
i=6
fun()
'''

#函数的嵌套调用
'''
def test1():
    print("*"*50)
    print("test1")
    print("*"*50)
def test2():
    print("-"*50)
    print("test2")
    test1()
    print("*"*50)
test2()
'''

'''
def print_line(char):
    print(char*50)

print_line("1")
'''
'''
def print_line(char,count):
    print(char*count)

print_line("1",10)
'''
'''
def print_line(char,count):
    print(char*count)

def print_lin(char,count):
    for i in range(5):
        print_line(char,count)
print_lin("1",3)
'''



























