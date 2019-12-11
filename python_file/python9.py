
'''
student=[{"name":"阿土",
            "age":20,
          "gender":True,
          "height":1.7,
          "weight":75.0},{
          "name":"小美",
          "age":19,
          "gender":False,
          "height":1.6,
          "weight":45.0 }]
find_name="阿土"
for stu_dict in student:
    print(stu_dict)
    #判断当前遍历的字典中姓名是否为find_name
    if stu_dict["name"]==find_name:
        print("找到了")
        #如果找到了，直接退出循环
        break
    else:
        print("没有找到")
print("循环结束")
'''

def Join(List,sep=None):
    return (sep or',').join(List)
print(Join(['a','b','c']))
print(Join(['a','b','c'],':'))
