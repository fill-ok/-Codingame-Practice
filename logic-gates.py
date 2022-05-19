# puzzle easy // https://www.codingame.com/ide/puzzle/logic-gates

# needed values
in_val = []
out_val = []
dic = {}
end = []

# game values
n = int(input())
m = int(input())
_ = int

# needed functions
def do_it(sol, letter, n):
    if n == False:
        sol = sol.replace('0','_').replace('1','-')
        end.append([letter+' '+sol])
    else:
        sol = sol.replace('0','-').replace('1','_')
        end.append([letter+' '+sol])
# game inputs
for i in range(n): 
    input_name, input_signal = input().split()
    input_signal = input_signal.replace('_','0').replace('-','1')
    dic[input_name] = (input_signal)

for i in range(m): 
    output_name, output_type, input_name_1, input_name_2 = input().split()
    out_val.append([output_name, output_type, input_name_1, input_name_2])

# game loop
for out in out_val:
    sol = ''

    # hold signals
    n1 = dic[out[2]]
    n2 = dic[out[3]]

    # bitwise operations
    if out[1] == 'AND':
        for f,s in zip(n1, n2):
            sol += str(_(f) & _(s))
        do_it(sol, out[0], False)

    if out[1] == 'OR':    
        for f,s in zip(n1, n2):
            sol += str(_(f) | _(s))
        do_it(sol, out[0], False)
    
    if out[1] == 'XOR':
        for f,s in zip(n1, n2):
            sol += str(_(f) ^ _(s))
        do_it(sol, out[0], False)
    
    if out[1] == 'NAND':
        for f,s in zip(n1, n2):
            sol += str(_(f) & _(s))
        do_it(sol, out[0], True)

    if out[1] == 'NOR':
        for f,s in zip(n1, n2):
            sol += str(_(f) | _(s))
        do_it(sol, out[0], True)
    
    if out[1] == 'NXOR':
        for f,s in zip(n1, n2):
            sol += str(_(f) ^ _(s))
        do_it(sol, out[0], True)

for _ in end: print(_[0])
