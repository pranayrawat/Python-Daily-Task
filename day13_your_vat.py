def your_vat():
    price = int(input("enter price of item: "))

    while True:
        try:
            vat = int(input("enter vat(%): "))
            if vat < 0:
                raise ValueError
            break
        except ValueError:
            print('Please enter positive number')
    
    price = price + ((price*vat)/100)
    return price
print(your_vat())