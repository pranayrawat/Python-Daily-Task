def largest_number(num1):
    str_list = [str(i) for i in num1]
    sep_list = []
    
    for i in str_list:
        length = len(i)
        for j in range(length):
            sep_list.append(int(i[j]))
    
    desc_list = sorted(sep_list,reverse = True)
    desc_list = [str(i) for i in desc_list]
    return int("".join(desc_list))

print(f"{largest_number([3,67,87,9,2]):,}")