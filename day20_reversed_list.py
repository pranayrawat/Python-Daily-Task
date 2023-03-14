def reversed_list(str):
    l = str.split(" ")
    upper = []
    
    for item in l:
        for c in item:
            if ord(c) >= 65 and ord(c) <= 90:
                upper.append(item)
                break
    
    rev = [item[::-1] for item in upper]
    return rev
    
print(reversed_list("""leArning is hard, bUt if You appLy youRself you can achieVe success"""))