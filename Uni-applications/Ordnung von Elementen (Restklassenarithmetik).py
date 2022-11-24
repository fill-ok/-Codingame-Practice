mod=13

for a in range(1,mod):
  t=0
  s=[]
  for k in range(1,mod):
    t=a**k %mod
    s.append(t)
  s=sorted(set(s))
  print(f'{a}={s,len(s)}')
  print(end='\n')
