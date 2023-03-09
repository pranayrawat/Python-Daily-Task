def equal_strings(s1,s2):
    not_eq = 0
    if len(s1) == len(s2):
        for i in range(len(s1)):
            if s1[i] in s2 and s2[i] in s1:
                pass
            else:
                not_eq += 1
    
    if not_eq > 0:
        return False
    
    return True
    
print(equal_strings("love","oelv"))