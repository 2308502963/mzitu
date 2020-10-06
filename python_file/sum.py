# n项累加求和（自然数）
def sum():
    print'输入n:'
    n=input("")
    sum=0
    while n<=0:
        print("input error!try again!")
        n=input("")
    for i in range(1,n+1):
        sum=sum+i
        return sum
    print(sum)
sum()
