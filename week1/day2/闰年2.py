a = int(input("请输入一个年份: "))
if((a > 1000 and a < 9999)):
    if((a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)):
        print(a,"是闰年",sep="")
    else:
        print(a,"不是闰年",sep="")
else:
    print("输入的年份不合法")