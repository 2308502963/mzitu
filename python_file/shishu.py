'''
#猜數字
guest=input("請輸入\n")
print("才{}了".format("對"if guest==99 else "錯"))
'''

#BMI
height,weight = input("請輸入您的身高(米)和體重(kg)(並用逗號隔開):\n")
BMI = weight/pow(height,2)
print("您的BMI指數是:{:.2f}".format(BMI))
person,nation="",""
if BMI<18.5:
    person,nation="偏瘦","偏瘦"
elif 18.5 <= BMI <24:
    person,nationn="正常","正常"
elif 24 <= BMI <25:
    person,nation = "正常","偏胖"
elif 25 <= BMI <28:
    person,nation = "偏胖","偏胖"
elif 28 <= BMI <30:
    person,nation = "胖","胖"
print("BMI指標為：國際{0},國内{1}".format(person,nation))


