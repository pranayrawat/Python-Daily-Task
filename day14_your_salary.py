def your_salary():
    global teacher
    teacher = input("teachers name: ")
    global periods
    periods = int(input("Periods taught: "))
    cur_rate = 20
    ot_rate = 25
    mon_sal = 0
    
    if periods < 100:
        mon_sal = periods * cur_rate
    else:
        mon_sal = (100*cur_rate) + ((periods-100)*ot_rate)
    
    return mon_sal
    
sal = your_salary()

print(f"Teacher: {teacher},\nPeriods: {periods}\nGross salary: {sal:,}")