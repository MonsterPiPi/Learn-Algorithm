print("输入某年某月某日，判断这一天是一年的第几天")
date = input('请输入某年某月某日，格式为 yyyy-mm-dd ：')
year = int(date[0:4])  #获取年份
month = int(date[5:7])  #获取月份
day = int(date[8:10])  #获取日

ly = False

if year % 100 == 0 : #若年份能被100整除
    if year % 400 == 0: #且能被400整除
        ly = True #则是闰年
        print(date+"是闰年")
    else:
        ly = False
        print(date + "不是闰年")
elif year % 4 ==0 :#其它情况下，若能被4整除
    ly = True #则是闰年
    print(date + "是闰年")
else:
    ly = False
    print(date + "不是闰年")


if ly == True:  #若为闰年，则2月份有29天
    ms = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    ms = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = 0
for i in range(1, 13):  #从1到12逐一判断，以确定月份
    if i == month:
        for j in range(i-1):  #确定月份i之后，则将ms列表中的前i-1项相加
            days += ms[j]
        print('%s是该年份的第%s天。' % (date, (days + day))) #最后再加上“日”，即是答案

