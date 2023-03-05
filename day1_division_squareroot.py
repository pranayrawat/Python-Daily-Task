import math

def division_or_square(number):
    if number % 5 == 0:
        return math.sqrt(number)
    else:
        return number % 5

print(division_or_square(9))