def sum_list(l1):
    l2 = []
    for i in l1:
        l2.extend(i)
    
    ans = sum(l2)
    return ans
    
print(sum_list([[2,4,5,6],[2,3,5,6]]))