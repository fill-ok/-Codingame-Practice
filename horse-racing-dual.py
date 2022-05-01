#  https://www.codingame.com/ide/puzzle/horse-racing-duals // puzzle easy

end,tmp=[],[]
for i in range(int(input())):end.append(int(input()))
for current, next in zip(end:=sorted(end,reverse=True),end[1:]):tmp.append(current-next)
print(sorted(tmp)[0])
