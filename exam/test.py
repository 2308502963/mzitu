# _*_ coding: utf-8 _*_
# @Time : 2019/12/14 17:59
# @Author : moran office
# File : test.py
# Software : PyChram

import re
import random


# a = ['name', 'age', 'sex']
# b = ['Dong', 38, 'Male']
# c = dict(zip(a, b))
# print(c)
# print('liujiang'.join(list('hello world!')))

# x = (3,)
# print(x)

# print([5 for i in range(10)])

# print('0'.join(list('hello world!')))

# a = [1, 2, 3]
# b = [1, 2, 4]
# print(id(a[2]) == id(b[2]))

# print(int('123', 16))   #把16进制的123转换成2进制

# print(type(reversed([1, 2, 3])))

# x = ['11', '2', '3']
# print(max(x, key=len))

# print(3 or 5)

# x = [3, 7, 5]
# x.sort(reverse=True)
# print(x)

# x = [3, 7, 5]
# x = x.sort(reverse=True)
# print(x)

# x = [3, 5, 3, 7]
# print([x.index(i) for i in x if i == 3])

# x = [3, 5, 7]
# x[:2] = [2]
# print(x)

# print(list(str([1, 2, 3])))

# print('Hello world. I like Python.'.rindex('Python'))
# # print('Hello world. I like Python.'.rfind('Python'))

# print(len('Hello world!'.ljust(20)))

# print(re.split('\.+', 'alpha.beta...gamma..delta'))

# print(re.findall('(\d)\\1+', '33abcd112'))

# x = list(range(5))
# x.remove(3)
# print(x)
# print(x.index(4))


# x = [1, 3, 2]
# x.reverse()
# print(x)

# x = [1, 3, 2]
# print(x.reverse())
# print(x)
# print(list(reversed(x)))
# print(x)

# x = [1, 3, 2]
# print(sorted(x))
# print(x.sort())

# x = [1, 3, 2]
# y = list(reversed(x))
# print(y)

# x = {0: 3, 1: 4, 2: 5}
# print(x.items())
# print(sum(item[0] for item in x.items()))

# s = 'hello world'
# with open('E:\\test.txt', 'a+') as f:
#     f.write(s)

# 编写程序，生成一个包含20个随机整数的列表，然后对其中偶数下标的元素进行降序排列，奇数下标的元素不变。
# list = [random.randint(0, 100) for i in range(20)]
# print(list)
# y = list[::2]
# y = sorted(y)
# list[::2] = y
# print(list)

# 编写函数，判断一个数字是否为素数，是则返回字符串YES，否则返回字符串NO。
# def panduan(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return "NO"
#     else:
#         return "YES"


# 编写函数，模拟Python内置函数sorted()
# def _sorted(li):
#     list = []
#     length = len(li)
#     l = li[0:]
#     print(l)
#     for i in range(length):
#         xiao = min(l)
#         list.append(xiao)
#         l.remove(xiao)
#     return list
# print(_sorted([-1, 2, 6, 0]))

# 编写程序，生成包含20个随机数的列表，然后将前10个元素升序排列，后10个元素降序排列，并输出结果
# list = [random.randint(0, 100) for i in range(20)]
# before = list[:10]
# after = list[10:]
# before = sorted(before)
# after = sorted(after, reverse=True)
# list[:10] = before
# list[10:] = after
# print(list)

# list = [random.randint(0, 100) for i in range(20)]
# list[:10] = sorted(list[:10])
# list[10:] = sorted(list[10:], reverse=True)
# print(list)

# n = input("输入整数:")
# print("{:->20,}".format(eval(n)))
# def funx(num):
#     global x
#     x *= 2
# x = 20
# funx(x)
# print(x)





