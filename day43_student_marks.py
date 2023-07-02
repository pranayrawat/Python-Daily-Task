def student_marks():
    name = []
    marks = []
    
    while True:
        temp = []
        name.append(input("name: "))    
        for i in range(3):
            temp.append(int(input(f"marks {i+1}:")))
        
        marks.append(temp)
        choice = input("want to enter more student data ?(yes/no): ")
        if choice == "no":
            break
    
    print(name)
    print(marks)
    
    data = dict()
    data = {name[i]: marks[i] for i in range(len(name))}
    print(data)
student_marks()