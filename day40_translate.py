def translate(s1):
    l1 = s1.split(" ")
    vowels = ['a','e','i','o','u']
    temp = []
    
    for i in l1:
        if i[0] in vowels:
            i = i + "yay"
            temp.append(i)
        
        else:
            i = i[1:] + i[0] + "ay"
            temp.append(i)
    
    return " ".join(temp)
            
print(translate('i love python'))