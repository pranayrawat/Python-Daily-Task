def repeated_name(l1):
    maxno = 1
    most_rep = ""
    for i in set(l1):
        if l1.count(i) > maxno:
            maxno = l1.count(i)
            most_rep = i
    return most_rep
    
    
print(repeated_name(["John","Peter","John","Peter","Jones","Peter"]))