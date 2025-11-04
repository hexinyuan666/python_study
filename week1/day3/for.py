#输入两个整数l和s，输出从l到s之间所有整数的和（包含l和s）
l = int(input("请输入第一个整数l: ")) 
s = int(input("请输入第二个整数s: "))
sum = 0
for i in range(l, s + 1,1):
    #代码块
    sum += i
print("从", l, "到", s, "之间所有整数的和为:", sum)





#输入一个整数n，输出从1到n之间所有的偶数
n = int(input("请输入一个整数n: "))
for i in range(1, n + 1, 1):
    if i % 2 == 0:
        print(i, end=" ")


