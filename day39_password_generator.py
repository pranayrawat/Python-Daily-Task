import string
import random

def password_generator():
    upperLetters = list(string.ascii_uppercase)
    lowerLetters = list(string.ascii_lowercase)
    digits = list(string.digits)
    punctuation = list(string.punctuation)
    temp = []
    
    print("Press 1 for weak")
    print("Press 2 for strong")
    print("Press 3 for very strong")
    passStrength = input("how much strong password you want: ")
    
    while True:
        
        if passStrength == "1":
            upper = random.sample(upperLetters,k=2)
            lower = list(random.choice(lowerLetters))
            number = list(random.choice(digits))
            punc = list(random.choice(punctuation))
            
            temp = upper+lower+number+punc
            random.shuffle(temp)
            print("Your generated password: ","".join(temp))
            break
        
        elif passStrength == "2":
            upper = random.sample(upperLetters,k=2)
            lower = random.sample(lowerLetters,k=3)
            number = random.sample(digits,k=2)
            punc = list(random.choice(punctuation))
            
            temp = upper+lower+number+punc
            random.shuffle(temp)
            print("Your generated password: ","".join(temp))
            break
            
        elif passStrength == "3":
            upper = random.sample(upperLetters,k=3)
            lower = random.sample(lowerLetters,k=4)
            number = random.sample(digits,k=3)
            punc = random.sample(punctuation,k=2)
            
            temp = upper+lower+number+punc
            random.shuffle(temp)
            print("Your generated password: ","".join(temp))
            break
        
        else:
            print("Wrong choice....try again")
            passStrength = input("how much strong password you want: ")
        
password_generator()