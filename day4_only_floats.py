def only_floats(num1,num2):
    if isinstance(num1,float) and isinstance(num2,float):
        return 2
    elif isinstance(num1,float) or isinstance(num2,float):
        return 1
    else:
        return 0
    

ans = only_floats(12.1,23)
print(ans)