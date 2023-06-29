import csv

content = []
digits = []
split = []
all_items = []
def just_digits():
    with open('python.csv',mode='r') as file:
        
        csvFile = csv.reader(file)
        
        for lines in csvFile:
            for item in lines:
                if item != " ":
                    content.append(item)
        
        for item in content:
            split.append(item.split(" "))
                
        for i in split:
            for j in i:
                all_items.append(j)
         
        for i in all_items:
            if i.isdigit():
                digits.append(i)
                
        print(digits)
just_digits()