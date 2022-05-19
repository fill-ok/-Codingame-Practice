# puzzle easy // https://www.codingame.com/ide/puzzle/sudoku-validator

# needed values
row_, column_, grid_3x3, sol = [], [], [], []
valid = [1, 2, 3, 4, 5, 6, 7, 8, 9]
subgrid = False

# needed functions
def check(arr):
    for _ in arr:
        tmp = valid.copy()

        for s in _: 
            if s in tmp: tmp.remove(s)
        if tmp != []: return False
    return True

# sudoku in [row][cal]
for i in range(9):
    tmp = []
    for j in input().split(): tmp.append(int(j))
    row_+=[tmp]

# sudoku in [cal][row]
for row in range(len(row_)): 
    tmp = []
    for cal in range(len(row_)): tmp.append(row_[cal][row])
    column_+=[tmp]

# sudoku in 3x3 subgrids
for _ in [[1,1],[1,4],[1,7],[4,1],[4,4],[4,7],[7,1],[7,4],[7,7]]:
    
    tmp = [row_[_[0]][_[1]]] # root 
    tmp.append(row_[_[0]-1][_[1]]); tmp.append(row_[_[0]+1][_[1]]) # up/ down
    tmp.append(row_[_[0]][_[1]+1]); tmp.append(row_[_[0]][_[1]-1]) # left/ right
    tmp.append(row_[_[0]-1][_[1]-1]); tmp.append(row_[_[0]-1][_[1]+1]) # diagonal up
    tmp.append(row_[_[0]+1][_[1]-1]); tmp.append(row_[_[0]+1][_[1]+1]) # diagonal down

    if sum(tmp) != 45: subgrid = False; break
    else: subgrid = True

# check if row and column values are different
for _ in [row_, column_]: sol.append(check(_))

# print solution
if sol[0] is True and sol[1] is True and subgrid is True: print('true')
else: print('false')
