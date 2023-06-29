def missing_numbers(l1):
    missing = [i for i in range(min(l1),max(l1)+1) if i not in l1]
    print(missing)
    
missing_numbers([1,2,3,5,6,8,9,11])