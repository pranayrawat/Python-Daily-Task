def longest_word(l1):
    max_len = 0
    for i in l1:
        if len(i) > max_len:
            tmp = []
            max_len = len(i)
            tmp.append(max_len)
            tmp.append(i)

    return tmp
    
print(longest_word(["Java","Javascript","Python"]))