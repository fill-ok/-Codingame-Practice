# https://www.codingame.com/ide/puzzle/offset-arrays // puzzle easy

from collections import defaultdict
import re

# needed values
hold = defaultdict(list)
ass = []

for i in range(n:=int(input())): 
    
    # find all letters
    letter = re.findall('[A-Z]+', ass:=input())

    # create a dict with 'letter' + 'conversion factor' + 'values of list'
    for i,_ in enumerate(ass.split('=')):
        h = list(map(int,re.findall('[\d-]+', _)))
     
        if i==0:
            if h[0] < 0: hold[letter[0]].append(abs(h[0]))
            if h[0] >= 0: hold[letter[0]].append(-abs(h[0]))

        else: hold[letter[0]].append(h)

# find all 'letters' and the 'start value'
rep = re.findall('[A-Z0-9-]+',x:=input())

# find the start value
first = hold[rep[-2]][1][int(rep[-1]) + hold[rep[-2]][0]]

# insert the calc value (in reverse)
for _ in rep[:len(rep)-2][::-1]: first = hold[_][1][first + hold[_][0]]

# print solution
print(first)
