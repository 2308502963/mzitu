#TempConvert.py
TempStr = input("请输入带有单位的温度值:")
if TempStr[-1] in ['F','f']:
    c = (eval(TempStr[0:-1])-32)/1.8
    print("转换之后的温度是:{:.2f}c".format(c))
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1])+32
    print("转换之后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")
    TempStr = input("请输入带有单位的温度值:")
    if TempStr[-1] in ['F','f']:
        c = (eval(TempStr[0:-1])-32)/1.8
        print("转换之后的温度是:{:.2f}F".format(c))
    elif TempStr[-1] in ['C','c']:
        F = 1.8*eval(TempStr[0:-1])+32
        print("转换之后的温度是{:.2f}F".format(F))
