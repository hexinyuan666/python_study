a=int(input())
b=int(input())
c=int(input())
#计算三角形的半周长
p=(a+b+c)/2
#求三角形面积
s = (p*(p-a)*(p-b)*(p-c))**0.5
print(s)