def even_or_average():
    nos = input("enter numbers separated by comma: ")
    l1 = [int(i) for i in nos.split(",")]
#     print(l1)
    count = 0
    even = []
    for i in l1:
        if i%2 == 0:
            even.append(i)
    if len(even) > 0:
        return max(even)
    else:
        return (sum(l1)/len(l1))
print(f"{even_or_average()}")