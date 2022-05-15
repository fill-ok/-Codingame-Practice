# puzzle easy // https://www.codingame.com/ide/puzzle/lumen

from collections import Counter

# game values
n = int(input())
l = int(input())

# needed values
kerz, pos_digit, end = [], [], []

for i,_ in enumerate([[cell for cell in input().split()] for i in range(n)]):
    for j,item in enumerate(_):
        if item == 'C': kerz.append([i,j])

# find all positions around a 'C'
for _ in kerz:
    for d in range(1,l):
        tmp = []
        tmp.append(_) # C as self
        tmp.append([_[0],_[1]-d]); tmp.append([_[0],_[1]+d]) # on row
  
        # remove all negative positions
        for t in tmp:
            if t[0]<n and t[0]>=0 and t[1]>=0 and t[1]<n: pos_digit.append(t)

    pos_digit = sorted(pos_digit)

    # p1 = min positon on diagonal
    p1 = pos_digit[0]
    if p1[0]-l < 0: p1[0] = 0
    else: p1[0] = p1[0]-(l-1) 

    # p2 = max positon on diagonal
    p2 = pos_digit[-1]
    if p2[0]+l >= n: p2[0] = n-1
    else: p2[0] = p2[0]+(l-1) 

    # fills the found square based on the size of p1 and p2
    for i in range(p1[0], p2[0]+1):
        for p in range(p1[1], p2[1]+1):
            if [i,p] not in end: end.append([i,p])

    pos_digit.clear()

# print solution
print(n*n-len(end))
