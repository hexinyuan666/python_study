a = int(input())
b = int(input())
c = int(input())


d = a==100 or b==100 or c==100
e = a>90 and b>90 or a>90 and c>90 or b>90 and c>90
f = a>80 and b>80 and c>80

ans = d or e or f
print(ans)
