# https://www.codingame.com/ide/puzzle/reverse-minesweeper // puzzle easy

from collections import Counter
import re

# needed values
sol, x_pos, end = [], [], []

# game values
w, h = int(input()), int(input())
for i in range(h): sol.append(input())

# find all positions of char 'x'
for r, row in enumerate(sol): 
    for c, col in enumerate(row):
        if col == 'x': x_pos.append([r,c])

# find all positions around a 'x'
for _ in x_pos:
    end.append([_[0],_[1]-1]); end.append([_[0],_[1]+1]) # on same row
    end.append([_[0]+1,_[1]]); end.append([_[0]-1,_[1]]) # on top /under row
    end.append([_[0]-1,_[1]-1]); end.append([_[0]-1,_[1]+1]) # on diagonal
    end.append([_[0]+1,_[1]+1]); end.append([_[0]+1,_[1]-1]) # on diagonal

# count all founded positions
end = list(map(str,end))
res = Counter(end)

# replace '.' with there count(value)
for rep in res.items():
    tmp = [int(_) for _ in re.findall('[\d-]+',rep[0])]

    if tmp[0] < h and tmp[0] >= 0 and tmp[1] < w and tmp[1] >= 0 and sol[tmp[0]][tmp[1]] != 'x':
        u = [_ for _ in sol[tmp[0]]]
        u[tmp[1]] = str(rep[1])
        sol[tmp[0]] = ''.join(u)

# remove all 'x'
for row in range(len(sol)): sol[row] = sol[row].replace('x','.')

# print solution
for _ in sol: print(_)
