def add_hash(str):
    l1 = list(str)
    leng = len(l1)
    l1.insert(int(leng/2),"#")
    return "".join(l1)
   
   
def add_underscore(str):
    str = str.replace("#","_")
    return str

def remove_underscore(str):
    str = str.replace("_","")
    return str

# print(add_hash("Python"))
# print(add_underscore(add_hash("Python")))
print(remove_underscore(add_underscore(add_hash("Python"))))