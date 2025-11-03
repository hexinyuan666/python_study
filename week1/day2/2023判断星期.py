b = int(input("请输入一个2023年的月份: "))
a = int(input("请输入该月份的日期: "))
# 判断月份和日期是否合法
if b >= 1 and b <= 12:
    if b in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif b in [4, 6, 9, 11]:
        max_day = 30
    else:  # b == 2
        max_day = 28
if a >= 1 and a <= max_day:
    # 计算该日期与1月1日之间的天数差
    total_days = 0
    for month in range(1, b):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            total_days += 31
        elif month in [4, 6, 9, 11]:
            total_days += 30
        else:  # month == 2
            total_days += 28
    total_days += a - 1
    week_day = (total_days % 7)
    if week_day == 0:
        print("2023年{}月{}日是星期日".format(b, a))
    elif week_day == 1:
        print("2023年{}月{}日是星期一".format(b, a))
    elif week_day == 2:
        print("2023年{}月{}日是星期二".format(b, a))
    elif week_day == 3:
        print("2023年{}月{}日是星期三".format(b, a))
    elif week_day == 4:
        print("2023年{}月{}日是星期四".format(b, a))
    elif week_day == 5:
        print("2023年{}月{}日是星期五".format(b, a))
    elif week_day == 6:
        print("2023年{}月{}日是星期六".format(b, a))
else:
    print("输入的日期不合法")