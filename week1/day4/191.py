n = int(input())
sum = 0

for i in range(1,n+1):
    for j in str(i):
        if j in '2019':
            sum+=i
            break

print(sum)