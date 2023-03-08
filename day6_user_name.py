def user_name():
    email = input("enter email: ")
    spl = email.split("@")
    return spl[0]
    
print(f"Username: {user_name()}")