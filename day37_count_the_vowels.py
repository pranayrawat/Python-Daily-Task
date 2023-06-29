def count_the_vowels(s1):
    upper_vowel = ['A','E','I','O','U']
    lower_vowel = ['a','e','i','o','u']
    
    vowel_found = set()
    
    upper_list = []
    lower_list = []
    
    for i in s1:
        if i in upper_vowel:
            vowel_found.add(i)
            
        if i in lower_vowel:
            vowel_found.add(i)
    
    for i in vowel_found:
        if i.isupper():
            upper_list.append(i)
        else:
            lower_list.append(i)
    
    print(f"Vowels found: {len(vowel_found)}")
    print(f"Upper Case Vowels found: {len(upper_list)}")
    print(f"Lower Case Vowels found: {len(lower_list)}")

count_the_vowels("hello")