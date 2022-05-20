# puzzle easy // https://www.codingame.com/ide/puzzle/create-the-longest-sequence-of-1s

from itertools import groupby

# needed values
sol, index = [], []
index = []

# game input
b = input()

# needed functions
def find(b):
    for key, iter in groupby(b):
        if key == '1': sol.append(len(list(iter)))

# find every index of value '0'
for i, c in enumerate(b): 
    if c == '0': index.append(i)

# replace every '0' with 1 and reset it
for i in index:
    tmp =  [_ for _ in b]
    tmp[i] = '1'
    tmp = ''.join(tmp)
    find(tmp)

# print solution
print(sorted(sol)[-1])
