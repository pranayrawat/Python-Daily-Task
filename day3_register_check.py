def register_check(dict1):
    
    count = 0
    for i in dict1.values():
        if i == 'yes':
            count += 1
    
    return count

present = register_check({'michael':'yes','john':'no','peter':'yes','mary':'yes'})
print("No of students in school:",present)