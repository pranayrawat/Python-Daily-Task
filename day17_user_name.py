import random

def user_name():
    name = input("enter name: ")
    l1 = list(name)
    l1.reverse()
    no = str(random.randint(0,9))
    l1.append(no)
    return "".join(l1)
    
print(f"username: {user_name()}")