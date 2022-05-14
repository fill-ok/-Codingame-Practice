# code golf // https://www.codingame.com/ide/puzzle/don't-panic 

# code size = 200

i,t=int,input;*E,=map(i,t().split());m=[E[4]]*E[0];exec('f,p=map(i,t().split());m[f]=p;'*E[-1])
while 1:C,p,d=t().split();e=m[i(C)];print(["WAIT","BLOCK"][i(p)<e and d[0]=="L"or i(p)>e and d[0]=="R"])
