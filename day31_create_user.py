def create_user():
    name = input("enter name: ")
    age = int(input("enter age: "))
    password = input("enter password: ")
    
    user_details = dict()
    user_details["name"] = name
    user_details["age"] = age
    user_details["password"] = password
    print("User saved.Please login")
    
    while True:
        check_name = input("name: ")
        check_password = input("password: ")
        
        if check_name == user_details['name'] and check_password == user_details['password']:
            print("Logged in successfully")
            break
        print("Wrong password or username. Please try again")
    
create_user()