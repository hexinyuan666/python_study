a = int(input())
b = int(input())

a = a + b%7
if(a>7):
    a = a%7
print(a)