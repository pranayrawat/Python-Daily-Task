def any_number(*args):
    sum = 0
    leng = len(args)
    for i in args:
        sum += i
    return sum/leng
    
print(any_number(12,90))