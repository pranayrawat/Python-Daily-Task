def count_words(str):
    l = str.split(" ")
#     print(f"{len(l)} words")
    return len(l)

def count_elements(str):
    l = str.split(" ")
    length = [len(i) for i in l]
    return sum(length)
    
#     Below is the one line code for same output
#     print(sum([len(i) for i in str.split(" ")]))
    
    
print(f"{count_words('I love learning')} words")
print(f"{count_elements('I love learning')} elements")

