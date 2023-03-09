def thousand_separator(l1):
    l2 = [f"{i:,}" for i in l1]    
    return l2
print(thousand_separator([1000000,2356989,2354672,9878098]))