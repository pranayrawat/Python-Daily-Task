def zeros_last(l1):
    
    if 0 in l1:
        c = l1.count(0)
        l2 = [i for i in l1 if i != 0]
        for i in range(c):
            l2.append(0)
        return l2
    else:
        l1.sort()
        return l1
# [2,1,4,7,6]
# [1,4,6,0,7,0,9]
print(zeros_last([2,1,4,7,6]))