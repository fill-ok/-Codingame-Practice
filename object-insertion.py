# puzzle easy // https://www.codingame.com/ide/puzzle/object-insertion 

# needed values
obj, grid, start, sol= [], [], [], []
count_star = 0

# game input()
row_all, cal_all = [int(i) for i in input().split()]
for i in range(row_all): obj.append(input())


c, d = [int(i) for i in input().split()]
for i in range(c): grid.append(input())

# count stars in obj[]
count_star = sum(_.count('*') for _ in obj)

# needed functions
def way(row_o, cal_o, row_g, cal_g):
    find = []

    for row, _ in enumerate(obj):
        for cal, val in enumerate(_):
            if val == '*':
                
                # map cal from ojb[] to grid[]
                if cal_o > cal: cal_g -= abs(cal_o - cal)
                if cal_o < cal: cal_g += abs(cal_o - cal)
                


                # [row][cal] have to be on grid
                if row_g+row<c and row_g+row>=0 and cal_g<d and cal_g>=0:
                    if grid[row_g + row][cal_g] == '.': 
                        
                        # update
                        cal_o = cal
                        
                        # sub solution founded
                        find.append([row_g+row, cal_g])
                    else: return False

    # append possible solution
    if len(find) == count_star: sol.append(find)

# game loop
for row_o, ro in enumerate(obj):
    for cal_o, co in enumerate(ro):
        if co == '*':

            for row_g, rg in enumerate(grid):
                for cal_g, cg in enumerate(rg):

                    # find possible start point
                    if cg == '.' and [row_g, cal_g] not in start:
                        start.append([row_g, cal_g])

                        # test start point of possible solution
                        way(row_o, cal_o, row_g, cal_g)

# print grind map
if len(sol) == 1:
    for _ in sol:
        for t in _:
            u = [i for i in grid[t[0]]]
            u[t[1]] = '*'
            grid[t[0]] = ''.join(u)
    print(1)
    for _ in grid: print(_)

# print value '0'
elif sol == []: print(0)

# print count of possible solutions
else: print(len(sol))
