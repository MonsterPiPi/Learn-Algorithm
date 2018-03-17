## Learn-Algorithm
学习算法，一周一更，基础语言为Python。
#### 输入某年某月某日，判断这一天是一年的第几天
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


#### 输入三个数，由小到大进行输出
    print("输入三个数，由小到大进行输出")
    a, b, c = input("输入a,b,c(空格分隔)").split()
    a, b, c = int(a), int(b), int(c)
    maxNo = max(a, b, c)
    minNo = min(a, b, c)
    print(maxNo, a+b+c-maxNo-minNo, minNo)
#### 求1到10000之内的完数
    print("求1到10000之内的完数")
    l = [ ]
    for n in range(1,10000):
        for a in range(1, n):
            if n % a == 0:
                l.append(a)
        if sum(l) == n:
            print(l)
            print(n)
        l = []