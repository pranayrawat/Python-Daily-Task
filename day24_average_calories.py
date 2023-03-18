def average_calories():
    calories = int(input("calories intake: "))
    days = int(input("no of days: "))
    return calories/days
    
print(f"Average Intake: {average_calories()} calories")