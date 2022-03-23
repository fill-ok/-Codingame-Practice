# puzzle easy // https://www.codingame.com/ide/puzzle/unary 

 37 lines (27 sloc) 724 Bytes
import itertools

# char -> decimal -> binary -> += every char in input()
l = [_ for _ in input()]
l = [bin(ord(_))[2:] for _ in l]

for item in range(len(l)):

    if len(l[item]) != 7:
        l[item] = '0' + l[item]
l = ''.join(l)

sep, str_ = [], ''

# separate difference parts in str(l)
for current_item, next_item in itertools.zip_longest(l,l[1:]):

    if current_item == next_item:
        str_ += current_item
    else:
        str_+= current_item
        sep.append(str_)
        str_ = ''

encode_str = ''

# encode sep[]
for item in sep:
    
    if item[0] == '1':
        encode_str += '0 '
    else:
        encode_str += '00 '
    encode_str += len(item) * '0'
    encode_str += ' '

print(encode_str[:-1])
