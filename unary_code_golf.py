# code golf // https://www.codingame.com/ide/puzzle/chuck-norris-codesize

# code size = 125
p=o=""
for e in"".join(map(lambda l:f"{ord(l):07b}",[*input()])):
 if e!=p:o+=(" 00 "," 0 ")[int(e)];p=e
 o+="0"
print(o[1:])
