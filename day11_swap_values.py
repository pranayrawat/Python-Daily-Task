def swap_values(l1):
    l1[0],l1[-1] = l1[-1],l1[0]
    return l1

    
print(swap_values([2,4,67,7]))