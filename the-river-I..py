# puzzle easy // https://www.codingame.com/ide/puzzle/the-river-i-

r1 = int(input())
r2 = int(input())

while r1 != r2:
    if r1<r2:
        r1+=sum(int(_) for _ in str(r1))
    else:
        r2+=sum(int(_) for _ in str(r2))
print(r1)
