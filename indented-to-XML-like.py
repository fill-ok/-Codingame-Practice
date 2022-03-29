# puzzle medium // https://www.codingame.com/contribute/view/805907680f5bef2e8167057ca832e79ab079

n, line, hold, list_space, l_except = int(input()), [], [], [], []
for i in range(n):
    line.append(input().split(':'))

# runs through line[]
for item in line:

    # delete the first spaces in item[1]
    if len(item) == 2 and item[1] != '':
        for _ in range(len(item[1])):
            if item[1][_] != ' ': item[1] = item[1][_:]; break

    #------------------------------- one line element---------------------------------
    if len(item) == 1:
        item_0 = ''
        
        for _ in  range(len(item[0])):
            if item[0][_] != ' ': item_0 = item[0][_:]; break
        item[0] = item[0].replace(item_0, '<'+item_0+'>')

         # check possible except item
        if 'print' in item[0]:
            space_count_ex = '', 0
            for _ in range(len(item[0])):
                    if item[0][_] != ' ': space_count_ex = _; break
            hold.insert(0, [space_count_ex, ''.join(item)[space_count_ex:]])

        else: print(item[0])

    # --------------------------------two line element----------------------------------
    elif item[1] != '':
        item_1 = ''

        for _ in range(len(item[0])):
            if item[0][_] != ' ': item_1 = item[0][_:]; break
        
        item[0] = item[0].replace(item_1, '<'+item_1+'>')
      
        for _ in range(len(item_1)):
            if item_1[_] == ' '    : item.append('</'+item_1[:_]+'>'); break
            elif _ == len(item_1)-1: item.append('</'+item_1[:len(item_1)]+'>'); break
        
        # check possible except item
        if 'ex' in item[0]:
            space_count_ex = '', 0
            for _ in range(len(item[0])):
                    if item[0][_] != ' ': space_count_ex = _; break
            hold.insert(0, [space_count_ex, ''.join(item)[space_count_ex:]])
            
        else: print(''.join(item))    

    # ----------------------------------container element---------------------------------
    else:
        # extract container item
        c_item, b_item, space_count = '', '', 0
        for _ in range(len(item[0])):
            if item[0][_] != ' ': c_item = item[0][_:]; space_count = _; break

        # extract the '</>' b_item
        for _ in range(len(c_item)):
            if c_item[_] == ' ': b_item = c_item[:_]; break
            else: b_item = c_item
        
        hold.insert(0, [space_count, '</'+b_item+'>'])
        list_space.insert(0, space_count)
     
        # print() -> '</>' items
        if len(hold) >= 2 and hold[0][0] == hold[1][0]:
            print(hold[1][0]*' '+hold[1][1])
            hold.pop(1)

        # if next == '0' container, than print(all) that are still in hold
        elif len(list_space) >= 2:
            for _ in range(2,len(list_space)):
                if space_count == list_space[_]:
                    
                    tmp = []
                    for _ in range(1, _):
                        print(hold[_][0]*' '+hold[_][1])
                        tmp.append(hold[_])

                    for _ in tmp:
                        hold.remove(_)
                        list_space.clear()
                    break
        # print 'start' of container
        print(space_count*' '+'<'+c_item+'>')

# set the 'except' item on the right position
for item_ex in hold:
    if 'ex' in item_ex[1]:
        hold = sorted(hold, reverse = True)

        for item in hold:
            if item_ex[0] == item[0]:
                ex, _ = hold.index(item_ex), hold.index(item)   
                hold[ex] = item
                hold[_] = item_ex

# set the 'print(result)' item on the right position
for item_pri in hold:
    if 'print' in item_pri[1]:
        
        for item in hold:
            if item_pri[0] == item[0]:
                pri, _ = hold.index(item_pri), hold.index(item)   
                hold[pri] = item
                hold[_] = item_pri

# empty the rest of the container
while  hold != []:
    print(hold[0][0]*' '+hold[0][1])
    hold.pop(0)
