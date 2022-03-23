# puzzle hard // https://www.codingame.com/ide/puzzle/depth-first-search-episode-2

from collections import defaultdict

# needed variables
start, founded, tmp_duplicate, try_only_1_times = 0, False, -1, False
l_links, g_pos, purple_nodes_equal_values = [], [], []
hold_all_gates_for_nodes, two_gates_dict = defaultdict(list), defaultdict(list)
shortest_way, purple_nodes, min_len_TGD_dict = defaultdict(list), defaultdict(list), defaultdict(list)
# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n_count, l_count, g_count = [int(i) for i in input().split()]
for i in range(l_count):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    l_links.append([n1,n2])
for i in range(g_count):
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

    def death_first_search(self,start):
        visited = [False]*n_count
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
full_dict = g.death_first_search(start)

# append every possible edge to every key...
for key in range(len(full_dict)): 
    for ele in range(len(full_dict)):
        if key in full_dict[ele] and key != ele:
            full_dict[key].append(ele)       
    
# delete duplicates of edges
for key in full_dict:
    full_dict[key] = list(set(full_dict[key]))

# find a adge between 2 gates
for pos_1 in range(len(g_pos)-1):
    for pos_2 in range(1,len(g_pos)):

        for _ in full_dict[g_pos[pos_1]]:

            if _ in full_dict[g_pos[pos_2]] and pos_1 != pos_2:
                two_gates_dict[_].append(g_pos[pos_1])
                two_gates_dict[_].append(g_pos[pos_2])

for node in two_gates_dict:
    two_gates_dict[node] = list(set(two_gates_dict[node]))
  
# find all gates for every node
for node in full_dict.keys():
    for gate in range(len(g_pos)):
        if node in full_dict[g_pos[gate]]:
            hold_all_gates_for_nodes[node].append(g_pos[gate])

# delete all 2gates in hold_all_gates_for_nodes[]
for _ in two_gates_dict:
    if _ in hold_all_gates_for_nodes:
        hold_all_gates_for_nodes.pop(_, None)

# -------------------------------------------------
# needed functions

# find shortest_path for given "start" & "goal"
def shortest_path(graph, start, goal):
    founded_ = []
     
    queue = [[start]]
    if start == goal:
        return
     
    while queue:    # Loop to traverse the graph with the help of the queue
        path = queue.pop(0)
        node = path[-1]
         
        if node not in founded_:
            neighbours = graph[node]

            for neighbour in neighbours:    #Loop to iterate over the neighbours of the node
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:
                    return new_path
            founded_.append(node)
    return

# count for a shortest_way[] the nodes that have only puplge adges
def count_purple_adges(short_path, key):

    c_purple = 1
    for current_ele in short_path:
    
        if current_ele in hold_all_gates_for_nodes.keys():
            c_purple+=1
        else: 
            c_purple-=1

    purple_nodes[key].append(c_purple)            

# test 5 -> find the max value len of a two_gates_dict{} item
def max_nodes_for_value_of_TGD(TGD, current_key):
    max_len_TGD = 0
    for item in TGD:
        max_len_TGD += len(full_dict[item])

    min_len_TGD_dict[current_key].append(max_len_TGD)
# -------------------------------------------------
i=0
# game loop
while True:
    founded = False

    bob = int(input())  # The index of the node on which the Bobnet agent is positioned this turn
    bob_list = full_dict[bob]

    purple_nodes.clear()
    purple_nodes_equal_values.clear()
    shortest_way.clear()

    while True:
        # ---------------find bob at nearest position to a gate <1>---------------

        for pos in range(len(g_pos)):

            if bob in full_dict[g_pos[pos]]:
        
                print(bob,g_pos[pos])  
               
                full_dict[g_pos[pos]].remove(bob)   # remove all founded adges
                full_dict[bob].remove(g_pos[pos])   # remove all founded adges

                hold_all_gates_for_nodes.pop(bob, None)   # remove all founded adges

                if bob in two_gates_dict: # remove all founded gates in two_gates_dict[]
                    two_gates_dict[bob].remove(two_gates_dict[bob][0])

                if two_gates_dict[bob] == []: two_gates_dict.pop(bob, None)

                founded = True
                break
        if founded == True: break
           
        # ---------------find shortest path for a node with 2 gates <3>---------------

        for two_gate in two_gates_dict:
            
            if two_gate != tmp_duplicate:

                tmp_list = shortest_path(full_dict, bob, two_gate)  # function call()
                tmp = ''.join(str(_) for _ in tmp_list)     # convert to a string
                    
                for _ in tmp_list:
                    shortest_way[two_gate].append(_)    # append string to given key = two_gate
            
        for key in shortest_way.keys():
                count_purple_adges(shortest_way[key], key)  # function call()

        # --------------- if two_gates_dict{} == empty / purple_nodes{} == empty -> try this <2>---------------
        if two_gates_dict == {} or purple_nodes == {}:

            for node in hold_all_gates_for_nodes:
                print(node, hold_all_gates_for_nodes[node][0])

                full_dict[node].remove(hold_all_gates_for_nodes[node][0])   # remove all founded adges
                full_dict[hold_all_gates_for_nodes[node][0]].remove(node)   # remove all founded adges
                hold_all_gates_for_nodes.pop(node, None)     # remove all founded adges

                tmp_duplicate = -1  # reset
                
                founded = True
                if founded == True: break  
            if founded == True: break  
        # ----------------------------------------------------------------------------------------------------       
        
        max_key, min_value = max(purple_nodes.items(), key = lambda x: x[1])    #give the min of purple_nodes

        # -------------------- <test> try to find a value that is equal to min_value in shortest_way{} ---------------
        purple_nodes_equal_values.append(max_key)   # needed if len(purple_nodes_equal_values) > 1 

        for key in purple_nodes:    
            if min_value == purple_nodes[key] and max_key != key: purple_nodes_equal_values.append(key)

        if len(purple_nodes_equal_values) > 1:
            min_of_all_values_in_PN = 1000
            min_key_PN = -1
            for key in purple_nodes_equal_values:

                if len(shortest_way[key]) < min_of_all_values_in_PN:    # test if current len(value) < min_of_all_values_in_PN

                    min_of_all_values_in_PN = len(shortest_way[key])
                    min_key_PN = key

            if min_key_PN != tmp_duplicate: max_key = min_key_PN   # set the founded min
        #-------------------------------------------------------------------------------------------------------------

        # -------------------- <test> try to find the max len of a value in two_gats_dict{} if len(TGD) <= 2 ---------
        if try_only_1_times == False and len(two_gates_dict) <= 2:
            for node in two_gates_dict:
                max_nodes_for_value_of_TGD(two_gates_dict[node], node)

            min_key_TGD, min_value_TGD = min(min_len_TGD_dict.items(), key = lambda x: x[1])

            try_only_1_times = True      

            if min_key_TGD != tmp_duplicate: max_key = min_key_TGD    
        #-------------------------------------------------------------------------------------------------------------
        
        tmp_duplicate = -1          # reset
        tmp_duplicate = max_key     # prevents that the same number printed by 2 times in serial

        print(max_key,two_gates_dict[max_key][0])

        full_dict[max_key].remove(two_gates_dict[max_key][0])   # remove all founded adges
        full_dict[two_gates_dict[max_key][0]].remove(max_key)   # remove all founded adges
        hold_all_gates_for_nodes.pop(bob, None)     # remove all founded adges

        two_gates_dict[max_key].remove(two_gates_dict[max_key][0])      # remove all founded adges

        if two_gates_dict[max_key] == []: two_gates_dict.pop(max_key, None)     # remove all empty keys

        founded = True
        if founded == True: break  
