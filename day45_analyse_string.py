import string

def analyse_string(s1):
    special_char = list(string.punctuation)
    temp = s1.split()
    t1 = temp.copy()
    
    for i in t1:
        if not i.isalpha():
            temp.remove(i)
    
    totalWords = len(temp)
   
    totalSpecialChar = 0
    for i in special_char:
        if s1.count(i) > 0:
            totalSpecialChar += s1.count("i")
    
    totalChar = len("".join(temp)) + totalSpecialChar
    
    summary = dict()
    summary["special character"] = totalSpecialChar
    summary["words"] = totalWords
    summary["total characters"] = totalChar
    
    return summary

s = 'Python has a string format operator %. This functions analogously to printf format strings in C, e.g. "spam=%s eggs=%d" % ("blah",2) evaluates to spam=blah eggs=2'

print(analyse_string(s))

