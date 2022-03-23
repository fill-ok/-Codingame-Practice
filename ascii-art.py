# puzzle easy // https://www.codingame.com/ide/puzzle/ascii-art

from collections import defaultdict
a_dict = defaultdict(list)

l = int(input())
h = int(input())
t, counter, pos, tmp_str = input().upper(), 0, 0, ''
a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ?'

# filter all sybomls that are not in str(a)
for _ in range(len(t)):
    if t[_] not in a: t = t.replace(t[_], '?')
    
# fill defaultdict{} with ' ' and lettes as keys
for key in range(len(a)):
    for y in range(h):
        matrix = [' ' for x in range(l)]
        a_dict[a[key]].append(matrix) 

# fill dict with t values
for i in range(h):
    row = input()
    counter = 0
    for key in a_dict.keys():
        for item in range(len(a_dict[key][pos])):
            
            a_dict[key][pos][item] = row[counter]
            counter+=1
    pos += 1

# print ASCII art
for row in range(h):
    for letter in t:
        tmp_str += ''.join(a_dict[letter][row])
    print(tmp_str)
    tmp_str = ''
