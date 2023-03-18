def nested_lists(*args):
    l1 = []
    for i in args:
        l1.append(i)
    return l1
    
print(nested_lists([1,2,3,5],[1,2,3,4],[1,3,4,5]))