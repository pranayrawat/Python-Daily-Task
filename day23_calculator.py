def add():
    try:
        return num1+num2
    except NameError:
        return "Some variable isn't defined."

def sub():
    try:
        return num1-num2
    except NameError:
        return "Some variable isn't defined."

def mul():
    try:
        return num1*num2
    except NameError:
        return "Some variable isn't defined."
    
def div():
    try:
        num1/num2
    except ZeroDivisionError as e:
        return "Cannot Divide by Zero"
    except NameError:
        return "Some variable isn't defined."
    
num1 = int(input("enter no 1: "))
num2 = int(input("enter no 2: "))

print("""
----------------------
Press 1 for addition
Press 2 for substraction
Press 3 for multiplication
Press 4 for division
----------------------
""")

while True:
    choice = input("enter your choice: ")
    
    if choice == "1":
        ans = add()
        break

    elif choice == "2":
        ans = sub()
        break
        
    elif choice == "3":
        ans = mul()
        break
        
    elif choice == "4":
        ans = div()
        break
       
    elif choice == "":
        print("Incorrect choice....try again")
        
    else:
        print("Incorrect choice....try again")
    
print(f"Answer: {ans}")