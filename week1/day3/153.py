#提取位数
n = int(input())
sum1 = 0
for i in range(1,n+1):
    a = i%10
    b = i//10 %10
    c = i//100 %10
    d = i//1000 %10
    e = i//10000 %10
    f = i//100000 %10
    if a!=2 and b!=2 and c!=2 and d!=2 and e!=2 and f!=2:
        sum1 +=1
print(sum1)




#用字符串检查
n = int(input())
sum1 = 0

for i in range(1, n+1):
    if '2' not in str(i):
        sum1 += 1

print(sum1)