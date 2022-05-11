# https://www.codingame.com/ide/puzzle/dungeons-and-maps // puzzle easy 

from collections import defaultdict

# given values
w, h = [int(i) for i in input().split()]
start_row, start_col = [int(i) for i in input().split()]
n = int(input())

# needed values
mapp = []
sol = defaultdict(list)
target = False

# game loop
for i in range(n):
    for j in range(h): mapp.append(input())
    
    x, y = start_col, start_row

    rnd = 0
    while True:
        rnd += 1

        if x>=w or y>=w or x<0 or y<0: target = False; break

        sym = mapp[y][x]
        if sym == '^': y-=1
        if sym == 'v': y+=1
        if sym == '<': x-=1
        if sym == '>': x+=1
        if sym == '.': target = False; break
        if sym == '#': target = False; break
        if sym == 'T': target = True ; break
        if x == start_col and y == start_row: target = False; break

    if target == True: sol[i].append(rnd)
    mapp.clear()
    
# print solution
sol = sorted(sol.items(), key = lambda x: x[1])
print(sol[0][0] if sol!=[] else 'TRAP')
