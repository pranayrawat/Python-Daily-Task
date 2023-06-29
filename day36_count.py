def count(s1):
    d1 = dict()
    l1 = list(set(s1))
    for i in l1:
        d1[i] = s1.count(i)
        
    c = s1.count("l")
    return d1

print(count("hello"))