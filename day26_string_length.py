def string_length(str):
    l1 = str.split()
    dict1 = dict()
    for i in l1:
        dict1[i] = len(i)
    return dict1
    
print(string_length("Hi my name is Richard"))