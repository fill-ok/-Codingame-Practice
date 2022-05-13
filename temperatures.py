# https://www.codingame.com/ide/puzzle/temperatures // puzzle easy

import collections
n=int(input()) 
t=[int(_)for _ in input().split()]
k=[-_ for _ in t if _<0];k+=[_ for _ in t if _>0]
f=[-_ for _, c in collections.Counter(k).items() if c > 1]
[t.remove(_) for _ in f]
print(min(t,key=abs) )if len(t)!=0 else print('0')
