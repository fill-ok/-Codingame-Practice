# https://www.codingame.com/ide/puzzle/asteroids // puzzle easy

import math
from collections import defaultdict 

# needed variables
f, s = [], []
coor = defaultdict(list)

w, h, t1, t2, t3 = [int(i) for i in input().split()]

for i in range(h):
    fp, sp = input().split()
    f.append(fp); s.append(sp)

# hold all letters in both 'skys'
fA = [_ for _ in ''.join(f) if _.isalpha()]

# create a empty 'sky'
thd = [''.join(['.']*w)]*w

# find every 'pos' of every 'letter' in every 'sky'
for letter in sorted(fA,reverse=True):
    for sky in [f,s]:
        for row in range(len(sky)):
            for cal in range(len(sky)):
                if sky[row][cal] == letter:
                    coor[letter].append([row,cal])

for let in coor.items():
    # calc new positon for the letter
    first = math.floor(((let[1][1][0]-let[1][0][0]) /(t2-t1)) *(t3-t2))
    sec   = math.floor(((let[1][1][1]-let[1][0][1]) /(t2-t1)) *(t3-t2))

    end = let[1][1][0] + first, let[1][1][1] + sec

    if end[0] < 0 or end[1] < 0 or end[0] >= w or end[1] >= w: pass
    else:
        # replace the founded pos with the letter
        u = [_ for _ in thd[end[0]]]
        u[end[1]] = let[0]
        thd[end[0]] = ''.join(u)

# print result
for _ in thd:print(_)
