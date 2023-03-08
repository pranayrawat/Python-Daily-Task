def names_count(names):
    l1 = [i for i in names if i[0] == 'S']
    s1 = set(l1)
    l2 = list(s1)
    l2.sort()
    d1 = dict()
    for name in l2:
        d1[name] = l1.count(name)
    return d1
    
print(names_count(['Joseph','Nathan','Sasha','Kelly',
             'Muhammad','Jabulani','Sera','Patel','Sera']))