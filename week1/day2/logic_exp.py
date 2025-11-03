#第一个例题 1>1 or 3<4 or 4>5 and 2>1 and 9>8 or 7<6
a = 1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
b = False or True or print("hello") #短路，不会打印hello
print(a)
print(b)
#第二个例题  not 2>1 and 3<4 or 4>5 and not 6<5
a = not 2 > 1 and 3 < 4 or 4 > 5 and not 6 < 5
b = False  or 4 > 5 and print("world") #短路，不会打印world
print(a)
print(b)
#运算符优先级
#算术运算符>关系运算符>逻辑运算符>赋值运算符