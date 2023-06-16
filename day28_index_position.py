def index_position(str1):
    index_list = [str1.index(i) for i in str1 if i.islower()]
    return index_list

print(index_position("LovE"))