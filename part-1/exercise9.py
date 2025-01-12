def merge(L1, L2):
    list_position_1 = 0
    list_position_2 = 0
    L = []
    
    if not L1 and not L2:
        return []
    
    while list_position_1 < len(L1) or list_position_2 < len(L2):
        if list_position_1 >= len(L1):  
            L.append(L2[list_position_2])
            list_position_2 += 1
        elif list_position_2 >= len(L2): 
            L.append(L1[list_position_1])
            list_position_1 += 1
        elif L1[list_position_1] <= L2[list_position_2]:
            L.append(L1[list_position_1])
            list_position_1 += 1
        else:
            L.append(L2[list_position_2])
            list_position_2 += 1
    
    return L


print(merge([0, 3, 6, 9, 12], [4, 6, 8, 10, 12, 14, 16]))
