def password_validator():
    password = input("enter password: ")
    
    upper = 0
    lower = 0
    length = len(password)
    number = 0
    
    while True:
        l1 = [i for i in password]
        
        for i in l1:
            if i.isupper():
                upper += 1
            elif i.islower():
                lower += 1
            elif i.isdigit():
                number += 1
        
        if length >= 8 and upper > 0 and lower > 0 and number > 0:
            print(f"Password is {password}")
            break
        else:
            if upper == 0:
                print("there should be atleast be one uppercase letter")
            if lower == 0:
                print("there should be atleast be one lowercase letter")
            if number == 0:
                print("there should be atleast be one number")
            if length < 8:
                print(length)
                print("Password should be of minimum 8 characters")
            
            password = input("Please enter another password: ")
    
password_validator()