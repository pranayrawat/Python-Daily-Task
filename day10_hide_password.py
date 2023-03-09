def hide_password():
    password = input("enter password: ")
    length = len(password)
    return "*"*(length-1)
    
ans = hide_password()
print(f"Your password {ans} is {len(ans)} characters long")