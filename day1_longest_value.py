def longest_value(a):
    l = [i for i in a.values()]
    length_list = [len(i) for i in a.values()]
#     print(l,"\n",length_list)

#     minimum = min(length_list)
    maximum = max(length_list)
    
#     print(minimum,maximum)

#   list comprehension below
    temp = [item for item in l if len(item) == maximum]

#     for item in l:
#         if len(item) == maximum:
#             temp.append(item)
#         else:
#             pass
    return temp[0]
    

print(longest_value({"fruit":"apple","color":"green"}))
