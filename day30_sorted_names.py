def sorted_names(l1):
    name_dict = dict()
    fname = [i.split(" ")[0] for i in l1]
    lname = [i.split(" ")[1] for i in l1]
    sorted_dict = dict()
    
    for i in range(len(l1)):
        name_dict[lname[i]] = fname[i]
    
    for i in sorted(name_dict.keys()):
        sorted_dict[i] = name_dict[i]
    
    final_list = [i + " " + sorted_dict[i] for i in sorted_dict]
    
    return final_list

print(sorted_names(["Beyonce Knowles","Alicia Keys","Katie Perry","Chris Brown","Tom Cruise"]))