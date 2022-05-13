# https://www.codingame.com/ide/puzzle/brain-fork // puzzle [optimization]

# needed values
zone = []
a = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
sol = ''
ii, zz = 0, 0

# declare the zone of 30 -> value '0'
for _ in  range(30): zone.append(0)

# needed fuctions
def find_min(min_):
    cpy = min_.copy()
    tmp = []

    for c in ['+','-']:
        sol_len = ''
       
        # exectuion of '+' or  '-' until letter is found
        while True:
            if _ == a[min_[1]]: break
            else:
                # case '+'
                if c == '+':
                    if    min_[1] + 1 >= 27: min_[1] = 0; sol_len += c
                    else: min_[1] += 1; sol_len += c

                # case '-'
                if c == '-':
                    if    min_[1] - 1 < 0: min_[1] = 26; sol_len += c
                    else: min_[1] -= 1; sol_len += c

        min_[1] = cpy[1]
        tmp.append(sol_len)
    
    if len(tmp[0]) < len(tmp[1]): return [cpy[0], cpy[1], tmp[0]]
    else: return [cpy[0], cpy[1], tmp[1]]

# game loop
for _ in input():

    # find 'best zone'
    min_ = [100, 100, '100']
    for i,z in enumerate(zone):
        tmp = find_min([i, z])

        if i == 0: 
            if len(tmp[2]) < int(min_[2]): min_ = tmp   
        else:      
            if len(tmp[2]) < len(min_[2]): min_ = tmp  


    # find min way to 'best zone'
    if   ii - min_[0] < 0: sol += '>' * abs(min_[0]-ii)
    elif ii - min_[0] > 0: sol += '<' * abs(min_[0]-ii)

    sol += min_[2]+'.'

    # update current zone 
    for _ in min_[2]:
        if min_[2][0] == '-': 
            if    min_[1] - 1 < 0: min_[1] = 26
            else: min_[1] -= 1; 


        if min_[2][0] == '+': 
            if    min_[1] + 1 >= 27: min_[1] = 0
            else: min_[1] += 1 

    # update zone[i]
    zone[min_[0]] = min_[1]
    ii, zz = min_[0], min_[1]

# print solution
print(sol)
