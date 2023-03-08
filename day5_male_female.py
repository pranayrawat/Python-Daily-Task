def male_female(students):
    lower_case = [i.lower() for i in students]
    male = [i for i in lower_case if i == 'male']
    female = [i for i in lower_case if i == 'female']
    
    return [("Male",len(male)),("Female",len(female))]

print(male_female(['Male','male','Female','FeMale','male','female','male','female','Male']))