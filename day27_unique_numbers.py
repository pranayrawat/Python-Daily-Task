def unique_numbers(l1):
    unique_list = []
    
    for i in l1:
        if l1.count(i) == 1:
            unique_list.append(i)
        
    sum_of_uniq = sum(unique_list)
    sum_of_orig = sum(l1)
    
    if abs(sum_of_orig - sum_of_uniq) % 2 == 0:
        return l1
    
    return unique_list

print(unique_numbers([1,2,4,5,6,7,8,8]))