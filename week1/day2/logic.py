#关系运算符都是双目运算符
#逻辑运算符中的or和and是双目运算符具有左结合性，not是单目运算符具有右结合性
#逻辑运算符的优先级：not > and > or
#or和and可以短路
#or的左边对时，结果为真，不再计算右边
#and的左边为假，结果为假，不再计算右边
url = "hello world"
print("----false and xxx----")
print(False and print(url))

print("----true and xxx----")
print(True and print(url))#继续计算右边
print("----true or xxx----")
print(True or print(url))#短路
print("----false or xxx----")
print(False or print(url))#继续计算右边
#逻辑运算符的结果不一定是布尔值，传回的是最后一个被计算的值