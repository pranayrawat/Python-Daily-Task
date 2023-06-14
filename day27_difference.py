def difference(l1,l2):
    
    # using + operator to concat two list
    final_list = [i for i in (set(l1)-set(l2))] + sorted([j for j in (set(l2)-set(l1))])
    
    return final_list

print(difference([1,2,4,5,6],[1,2,5,7,9]))