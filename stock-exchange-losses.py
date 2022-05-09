# https://www.codingame.com/ide/puzzle/stock-exchange-losses // puzzle medium

n=input()
tmp,max_=[],-1
for _ in  [int(_) for _ in input().split()]:
 if _>max_: max_=_
 tmp.append(max_-_)
print(-abs(max(tmp)))
