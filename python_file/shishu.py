'''
#����
guest=input("Ոݔ��\n")
print("��{}��".format("��"if guest==99 else "�e"))
'''

#BMI
height,weight = input("Ոݔ���������(��)���w��(kg)(�K�ö�̖���_):\n")
BMI = weight/pow(height,2)
print("����BMIָ����:{:.2f}".format(BMI))
person,nation="",""
if BMI<18.5:
    person,nation="ƫ��","ƫ��"
elif 18.5 <= BMI <24:
    person,nationn="����","����"
elif 24 <= BMI <25:
    person,nation = "����","ƫ��"
elif 25 <= BMI <28:
    person,nation = "ƫ��","ƫ��"
elif 28 <= BMI <30:
    person,nation = "��","��"
print("BMIָ�˞飺���H{0},����{1}".format(person,nation))


