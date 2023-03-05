def check_duplicates(list1):
    
    set1 = set()
    
    for item in list1:
        c = list1.count(item)
        if c > 1:
            set1.add(item)
        
    l1 = list(set1)
    l1.sort()
    if len(l1) > 0:
        return " ".join(l1)
    else:
        return "No duplicates"

print(check_duplicates(['apple','banana','orange','banana']))
