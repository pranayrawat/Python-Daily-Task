def check_pangram(s1):
    l1 = [i for i in list(s1) if i != " "]
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    count = 0
    for i in alphabets:
        if i in l1:
            count+=1
    if count == 26:
        return True
    else:
        return False
#l3 = [*s1]   # unpack method
#     l4 = [i for i in s1 if i != " "] #method 2
#     l2 = list(s1)

print(check_pangram("the quick brown fox jumps over a lazy dog"))