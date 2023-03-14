def sort_length(l1):
    for i in range(len(l1)):
        for j in range(i+1,len(l1)):
            if len(l1[i]) > len(l1[j]):
                l1[i],l1[j] = l1[j],l1[i]
    print(l1)


# ['Peter','Jon','Andrew']
# ['Jon','Peter','Andrew']
# ['Andrew','Peter','Jon']
sort_length(['Andrew','Peter','Jon'])