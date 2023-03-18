def multiply_words(str):
    l1 = str.split(" ")
    ans = 1
    count = 0
    for i in l1:
        if i.islower():
            ans = ans*len(i)
        else:
            count +=1
    
    if count == len(l1):
        return 0
    return ans
    
print(multiply_words("Hate war love Peace"))