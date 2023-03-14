def add_reverse(l1,l2):
    sum = []
    for i,j in zip(l1,l2):
        sum.append(i+j)
    
    print(sum)
    sum.insert(0,sum.pop(-1))
    print(sum)
    
add_reverse([10,12,34],[12,56,78])