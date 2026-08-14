year=int(input("请输入当前年份："))
if year%4==0 and year%100!=0 or year%400==0:
    print(year,"为闰年")
else:
    print(year,"为平年")
