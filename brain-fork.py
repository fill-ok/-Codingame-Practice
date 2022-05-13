# https://www.codingame.com/ide/puzzle/brain-fork // puzzle [unknown]

# needed values
zone = []
a = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
sol = ''
ii, zz = 0, 0

# declare the zone of 30 -> value '0'
for _ in  range(30): zone.append(0)

# game loop
for _ in input():

    # find 'best zone'
    min_ = [100, 100]
    for i,z in enumerate(zone):
        if abs(a.index(_)-z) < min_[1] : 
            min_ = [i,z]

    # find min way to 'best zone'
    if   ii - min_[0] < 0: sol += '>' * abs(min_[0]-ii)
    elif ii - min_[0] > 0: sol += '<' * abs(min_[0]-ii)

    # find min way 'best zone' to searched letter
    c = ''
    if   min_[1] - a.index(_) <  0: c = '+'
    elif min_[1] - a.index(_) >= 0: c = '-'
  
    # exectuion of '+' or  '-' until letter is found
    while True:
        if _ == a[min_[1]]: 
            sol += '.'
            break
        else:
            # case '+'
            if c == '+':
                if    min_[1] + 1 >= 27: min_[1] = 0; sol += c
                else: min_[1] += 1; sol += c

            # case '-'
            if c == '-':
                if    min_[1] - 1 < 0: min_[1] = 26; sol += c
                else: min_[1] -= 1; sol += c

    # update zone[i]
    zone[min_[0]] = min_[1]
    ii, zz = min_[0], min_[1]

# print solution
print(sol)
