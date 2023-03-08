def zeroed(num):
    num.pop(0)
    num.insert(0,0)
    
    num.pop(-1)
    num.append(0)
    
    return num
    
print(f"{zeroed([2,5,7,8,9])}")