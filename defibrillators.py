# https://www.codingame.com/ide/puzzle/defibrillators // puzzle easy

import math
from collections import defaultdict

lon = float(input().replace(',','.'))
lat = float(input().replace(',','.'))

item, val = defaultdict(list), []

for i in range(int(input())):
    defib = input().split(';')

    defib[-1] = float(defib[-1].replace(',','.'))
    defib[-2] = float(defib[-2].replace(',','.'))

    item[defib[1]].append(((((defib[-2]-lon)**2)+((defib[-1]-lat)**2))**0.5)*6371)

print(sorted(item.items(),key=lambda x:x[1])[0][0])
