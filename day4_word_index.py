def word_index(l1):
    length = len(l1[0])
    count = len(l1)
    element_len = [len(item) for item in l1]
    same_len = [length]*count
    
#     print(f"{element_len}\n{same_len}")
    
    ans = 0
    
    if element_len != same_len:
        a = len(l1[0])
        for item in l1:
            if len(item) > a:
                a = len(item)
                ans = l1.index(item)
    else:
        return 0
    return ans

# word_index(['hate','remorse','vengeance'])
# ['hate','hate']

print(word_index(['hate','hate']))