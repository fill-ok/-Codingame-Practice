# puzzle easy // https://www.codingame.com/ide/puzzle/1d-spreadsheet

import functools

n, hold = int(input()), []

# preparations
for i in range(n):
    op, a1, a2 = input().split()
    hold.append([op, a1, a2])

sol, c = ['?'] * len(hold), 0

# calculate the value and delete it in hold[] and append it in sol[]
def append_sol(item, tmp):
    if   item[0][0] == 'V': sol[hold.index(item)] = tmp[0]; hold[hold.index(item)] = '!'
    elif item[0][0] == 'A': sol[hold.index(item)] = functools.reduce(lambda a, b: a+b, tmp); hold[hold.index(item)] = '!'
    elif item[0][0] == 'S': sol[hold.index(item)] = functools.reduce(lambda a, b: a-b, tmp); hold[hold.index(item)] = '!'
    elif item[0][0] == 'M': sol[hold.index(item)] = functools.reduce(lambda a, b: a*b, tmp); hold[hold.index(item)] = '!'

# try it until every item in sol[] is != '?'
while True:
    for item in hold:
        error = False
        tmp=[]
        for val in item[1:]:

            # check if a given reference are exists 
            if '$' in val:
                if sol[int(val[1:])] != '?': tmp.append(sol[int(val[1:])])  # reference -> exists
                else: error = True; break   # reference -> don't exists
            elif val != '_': tmp.append(int(val))   # append absolut value to tmp[]

        if tmp != [] and error == False: append_sol(item, tmp)  # calc founded values -> located in tmp[]
        
    if '?' not in sol: break

# print solution
for _ in sol: print(_)
