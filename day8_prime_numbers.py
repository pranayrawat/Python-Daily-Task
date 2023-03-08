def prime_numbers():
    no = int(input("enter no: "))
    pr_no = []
    
    for i in range(2,no):
        count = 0
        for j in range(1,i+1):
            if i%1 == 0 and i%j == 0:
                count = count+1
        
        if count == 2:
            pr_no.append(i)
    return pr_no
    
print(prime_numbers())