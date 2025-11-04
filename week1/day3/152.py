d = int(input())
a,b,c=map(int,input().split())
e = 0

for i in range(1,1+d):
    if i%a!=0 and i%b!=0 and i%c!=0:
        e+=1
print(e)