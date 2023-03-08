def odd_even(num):
    even = max([i for i in num if i%2 == 0])
    odd = min([i for i in num if i%2 != 0])
    return even-odd
print(odd_even([1,2,4,6]))