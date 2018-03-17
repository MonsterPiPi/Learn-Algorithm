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