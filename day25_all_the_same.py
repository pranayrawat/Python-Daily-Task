def all_the_same(l1):
    length = len(l1)
    a = l1[0]
    l2 = [a]*length
    return l1 == l2
    
print(all_the_same(['Mary','Mary','Mary']))