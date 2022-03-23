# puzzle medium // https://www.codingame.com/ide/puzzle/depth-first-search-episode-1

from collections import defaultdict

# needed variables
gate = n1 = n2 = -1
l_links, g_pos, check = [],[],[]

# game input()
n, links, ex = [int(i) for i in input().split()]
for i in range(links):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    l_links.append([n1,n2])

for i in range(ex):
    gate = int(input())  # the index of a gateway node
    g_pos.append(gate)

#-------------------------------------------------
# algorithm to find every possible edge
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.graph[v].remove(u)

    def breitensuche(self,start):
        visited = [False]*n
        queue = [start]
        visited[start] = True

        while len(queue) > 0:
            start = queue.pop(0)

            for i in self.graph[start]:
                if visited[i]:
                    continue
                queue.append(i)
                visited[i] = True
        return self.graph
g=Graph()
#-------------------------------------------------

# find every edge and save it in full_dict[]
for i in range(len(l_links)):
    g.add(l_links[i][0],l_links[i][1])
full_dict = g.breitensuche(gate)

# append every possible edge to every key...
for key in range(len(full_dict)): 
    for ele in range(len(full_dict)):
        if key in full_dict[ele] and key != ele:
            full_dict[key].append(ele)       
    
# delete duplicates of edges
for key in range(len(full_dict)):
    full_dict[key] = list(set(full_dict[key]))

# -------------------------------------------------
while True:
    bob = int(input())
    bob_list = full_dict[bob]

    i=0

    if len(g_pos) == 1: # if count of gates are == 1
        g_list = full_dict[gate]    # create a tmp list of fulldict[gate]
    
        for _ in range(len(bob_list)):
            if bob in g_list:   # if bob in tmp g_list[]      
                print(bob,gate)     
               
                full_dict[gate].remove(bob)     # remove() the located adge in full_dict[gate]
                full_dict[bob].remove(gate)     # remove() the located adge in full_dict[bob]
                break 
            
            elif bob_list[_] in g_list: # try it if bob not directly in g_list[]
                print(bob_list[_],gate)
            
                full_dict[gate].remove(bob_list[_])     # remove() the located adge in full_dict[gate]
                full_dict[bob].remove(bob_list[_])      # remove() the located adge in full_dict[bob]
                break

    else:         
        for pos in range(len(g_pos)):

            if [bob,g_pos[pos]] in check:   # check if a adge already used
                print(bob,max(bob_list))    # print "bob" and his max(value) in bob_list[]
                break

            elif bob in full_dict[g_pos[pos]]:  # check if bob 1 adge in front of a gate
                print(bob,g_pos[pos])   # print located adge
                check.append([bob,g_pos[pos]])  # append located adge to check[]
               
                full_dict[g_pos[pos]].remove(bob)   # remove() located gate adge from full_dict[]
                full_dict[bob].remove(g_pos[pos])   # remove() located bob adge from full_dict[]  
                break
            i+=1
            if i>=3:    # try 3 times the above if: statement before test the following...
                for _ in range(len(bob_list)):  # try every single element in bob_list[]
                    if [bob_list[_],g_pos[pos]] in check:
                        print(bob,max(bob_list))
                        break

                    elif bob_list[_] in full_dict[g_pos[pos]]:
                        print(bob_list[_],g_pos[pos])
                        check.append([bob_list[_],g_pos[pos]])
                        
                        full_dict[g_pos[pos]].remove(bob_list[_])
                        full_dict[bob].remove(bob_list[_])
                        break
