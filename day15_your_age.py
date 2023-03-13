def your_age():
    names = {'jane':23,'kerry':45,'tim':34,'peter':27}
    stud = input("enter name: ").lower()
    
    if stud not in names.keys():
        print("your name is not in dictionary")
        age = int(input("enter your age: "))
        names[stud] = age
        print(f"Hi, {stud}, you are {age} years old")
    else:
        print(f"Hi, {stud}, you are {names[stud]} years old")
your_age()
