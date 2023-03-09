import datetime
def age_in_minutes():
    cur_year = int(datetime.datetime.now().year)
    while True:
        byear = input("enter birth year: ")
        if len(byear) == 4:
            if int(byear) < 1900 or int(byear) > cur_year:
                print("enter valid year")
            else:
                age = cur_year - int(byear)
                break
        else:
            print("enter year in 4 digits")
    return age*525600
    
print(age_in_minutes())