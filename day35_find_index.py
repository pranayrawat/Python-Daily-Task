def find_index(l1,no):
    idx = []
    length = len(l1)
    if no in l1:
        for i in range(len(l1)):
            if l1[i] == no:
                idx.append(i)
    else:
        idx = [no for i in range(len(l1))]
    
    return idx
print(find_index([1,2,4,6,7,7],7))