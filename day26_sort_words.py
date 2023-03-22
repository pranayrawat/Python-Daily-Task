def sort_words(str):
    l1 = list(str)
    s1 = set(l1)
    l1 = list(s1)
    l1.remove(" ")
    l1.sort()
    return l1

print(sort_words("love life"))