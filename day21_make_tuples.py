def make_tuples(l1,l2):
    l3 = [i for i in zip(l1,l2)]
    return l3
    
print(make_tuples([1,2,3,4],[5,6,7,8]))