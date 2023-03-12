def flat_list(l1):
    tmp = []
    for i in l1:
        tmp.extend(i)
        
    return tmp
print(flat_list([[1],[2,3],[4,5,6,7]]))