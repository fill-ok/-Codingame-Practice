# https://www.codingame.com/ide/puzzle/encryptiondecryption-of-enigma-machine // puzzle easy

operation = input()
rotor, alpha = [], 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n = int(input())

for i in range(3): rotor.append(input())
mes = input()

def encode(mes, rotor):
    end, s = '', '' ; c = 0

    for _ in mes:
        if alpha.find(_)+n+c > 25 and alpha.find(_)+n+c <=50: s += alpha[alpha.find(_)+n+c-26]
        elif alpha.find(_)+n+c > 50: s += alpha[alpha.find(_)+n+c-52]
        else: s += alpha[alpha.find(_)+n+c]
        c+=1

    for r in rotor:
        for item in s:
            if alpha.find(item) > 25: end += r[alpha.find(item)-25]
            else: end += r[alpha.find(item)]
        s = end
        end = ''
    return s

def decode(mes, rotor):
    end=''; c=0

    for r in rotor[::-1]:
        for item in mes:
            end += alpha[r.find(item)]
        mes = end
        end = ''  

    for item in mes:
        if alpha.find(item)-n-c < 0 and alpha.find(item)-n-c >= -26: end += alpha[26 + alpha.find(item)-n-c]
        elif alpha.find(item)-n-c < -25: end += alpha[52 + alpha.find(item)-n-c]
        else: end += alpha[alpha.find(item)-n-c]
        c+=1
    return end

print(encode(mes, rotor) if operation == 'ENCODE' else decode(mes, rotor))
