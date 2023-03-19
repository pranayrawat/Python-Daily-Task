def read_backwards(str):
    l1 = str.split()
    l1.reverse()
    return " ".join(l1)
    
print(read_backwards("the love is real"))