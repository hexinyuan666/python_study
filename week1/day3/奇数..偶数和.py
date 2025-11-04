a = int(input("请输入一个整数n: "))
res1,res2 = 0,0
for i in range(1, a + 1):
    if i % 2 == 0:
        res1 += i
    else:
        res2 += i
print("从1到", a, "之间所有偶数的和为:", res1)
print("从1到", a, "之间所有奇数的和为:", res2)