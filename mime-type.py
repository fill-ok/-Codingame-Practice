# https://www.codingame.com/ide/puzzle/mime-type // puzzle easy

from collections import defaultdict
import itertools

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

# needed var
data = defaultdict(list)
p_val = []

for i in range(n):
    ext, mt = input().split() # ext: file extension # mt: MIME type.
    data[ext.lower()].append(mt)

for i in range(q):
    fname = input().lower().replace('..','.').split('.')

    if len(fname)>1:
        if fname[len(fname)-1] in data.keys(): p_val.append(''.join(data[fname[len(fname)-1]]))
        else: p_val.append('UNKNOWN')
    else: p_val.append('UNKNOWN')

for _ in p_val: print(_)
