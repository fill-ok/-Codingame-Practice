https://www.codingame.com/ide/puzzle/roller-coaster // puzzle hard

# l = anzahl plätze
# c = pro Tag
# n = anzahl gruppe

# needed val
que = []
dirham = 0
counter = 0
ka=[]
# game input()
l, c, n = [int(i) for i in input().split()]
for i in range(n):que.append(int(input()))
cpy = que.copy()

for times in range(1,c+1):

    check_seat = 0
    for group in que:

        if check_seat + group <= l:
            check_seat += group

            cpy.append(cpy[0])
            del cpy[0]
        else: break

    que=cpy.copy()
        
    dirham+=check_seat

print(dirham)
