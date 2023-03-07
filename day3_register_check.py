def register_check(dict_1):
    l1 = []
    for val in dict_1.values():
        l1.append(val)
    
    present = l1.count('yes')
    return present

print(f"No of students present: {register_check({'michael':'yes','john':'no','peter':'yes','mary':'yes'})}")