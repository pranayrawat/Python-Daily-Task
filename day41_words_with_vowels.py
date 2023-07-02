def words_with_vowels(s1):
    l1 = s1.split(" ")
    vowels = ['a','e','i','o','u']
    ans = []
    
    for i in l1:
        for j in i:
            if j in vowels:
                ans.append(i)
                break
    print(ans)
    
words_with_vowels("you have no rhythm")