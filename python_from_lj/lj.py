# _*_ coding: utf-8 _*_
# @Time : 2019/12/5 13:30
# @Author : moran office
# File : lj.py
# Software : PyChram

import os
def display_function():
    print("-" * 33)
    print("    ****学生成绩管理系统****")
    print("    1.新增学生成绩信息\n    2.显示全部信息\n    3.查询\n    0.退出系统")
    print("-" * 33)
def add_list():    #添加用户信息
    flag=True
    while (flag):
     stu_name = input("请您输入姓名：")
     stu_num=input("请你输入学号：")
     stu_chinese = input("请您输入语文成绩：")
     stu_math = input("请您输入数学成绩：")
     stu_english = input("请您输入英语成绩：")
     chioce=input("是否继续添加Y/N:")
     new = {}
     new['姓名'] = stu_name
     new['学号']=stu_num
     new['语文'] = stu_chinese
     new['数学'] = stu_math
     new['英语'] = stu_english
     stu_info.append(new)
     save_stu()
     print("添加学生成绩成功！")
     if(chioce=='Y'):
      flag=True
     else:
      flag=False
def save_stu():  #保存用户信息到文件
    student=str(stu_info)
    with open("stu_information.txt","w",encoding="utf-8") as f:
        f.write(student)
        #print("保存成功！文件位置在"+os.getcwd())
def recover_data():  #恢复数据
    global stu_info
    try:
        with open("stu_information.txt","r",encoding="utf-8")as f:
            content=f.read()
            if content!='':
                user_info=eval(content)
    except:
        f=open("stu_information.txt","w")
        f.write("[]")
def print_all_info():    #显示全部学生成绩信息
    print("姓名\t\t\t学号\t\t\t\t语文成绩\t\t\t数学成绩\t\t\t\t英语成绩\t\t\t")
    for i in range(0, len(stu_info)):
        # print_kwargs(**user_card[i])
        print("{:<16}{:<16}{:<16}{:<16}{:<16}".format(stu_info[i]['姓名'], stu_info[i]['学号'],stu_info[i]['语文'], stu_info[i]['数学'],                                                            stu_info[i]['英语'],))
def find():  #查询学生成绩
    find_stu_name = input("请输入您要查找的用户的姓名：")
    find_num = 0
    can_not_find = 0
    for i in stu_info:
        if i['姓名'] == find_stu_name:
            find_num = stu_info.index(i)
            print("找到了，信息如下")
            print(i)
            can_not_find = 1
            break
    if can_not_find == 0:
        print("您查找的用户不存在！")
        return find()
    inp_find = int(input("【1】修改\n【2】删除\n【3】返回上一级菜单"))
    if inp_find == 1:
        stu_change_key = input("请输入需要修改的类别：")
        stu_change_value = input("请输入新内容：")
        stu_info[find_num][stu_change_key] = stu_change_value
        save_stu()
        print("修改成功！")
        print(stu_info[find_num])
    elif inp_find == 2:
        del stu_info[find_num]
        save_stu()
        print("删除成功！")
        print_all_info()
    elif inp_find == 3:
         main_code()
    else:
        print("输入有误，请重新输入！")
def main_code(): #主函数
    recover_data()
    while 1:
        display_function()
        user_doing = int(input("请输入您希望执行的操作："))
        if user_doing == 1:
            add_list()
        elif user_doing == 2:
            print_all_info()
        elif user_doing == 3:
            find()
        elif user_doing == 0:
            print("退出系统！")
        else:
            print("请输入正确的数值！")
            display_function()
    return

stu_info = []
main_code()