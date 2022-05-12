# https://www.codingame.com/ide/puzzle/prefix-code // puzzle easy

from collections import defaultdict

# needed variables
encode = defaultdict(list)
end, tmp = '', ''

# game variables
for i in range(n:=int(input())):
    inputs = input().split()
    encode[inputs[0]].append(chr(int(inputs[1])))

# if n == 0 -> fail
if n==0:print(f'DECODE FAIL AT INDEX {0}'); quit()

# sort encode[] by length of key(): small -> large
encode = sorted(encode.items(), key = lambda x: len(x[0]))


# decode string
for i, _ in enumerate(s:=input()):
    tmp += _

    if i == len(s)-1 and len(tmp) < len(encode[0][0]):
        print(f'DECODE FAIL AT INDEX {i}')
        quit()

    for e in encode:
        if e[0] == tmp:
            end += ''.join(e[1])
            tmp = ''
            break
        
        else: not_found = True

# print solution
print(end if end!='' and n!=0 else f'DECODE FAIL AT INDEX {0}')
