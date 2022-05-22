# puzzle easy // https://www.codingame.com/ide/puzzle/happy-numbers

for i in range(int(input())):
    num=input()
    x, i = [], 0
    while x!='1':
        if i==0: x=[int(_) for _ in  num]
        else: x=[int(_) for _ in  x]
        x=str(sum(map(lambda x:x**2,x)))
        if i==100:print(num, ':(');break
        i+=1
    if i<100:print(num,':)')
