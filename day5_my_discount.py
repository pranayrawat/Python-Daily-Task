def my_discount():
    price = int(input("enter price: "))
    discount = int(input("enter discount: "))
    
    final_price = price - ((price*discount)/100)
    
    return final_price

print(my_discount())