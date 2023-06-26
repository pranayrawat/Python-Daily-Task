def inter_section(l1,l2):
    s1 = set(l1)
    s2 = set(l2)
    
    # did below type casting to get output in ascending order and final output in tuple
    return tuple(sorted(list(s1.intersection(s2))))
    
print(inter_section([20,30,60,65,75,80,85],[42,30,80,65,68,88,95]))