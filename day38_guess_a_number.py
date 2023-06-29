import random

def guess_a_number():
    count = 1
    correct = random.randrange(1,5)
    
    while count<=3:
        user_ans = int(input("guess no: "))
        if user_ans == correct:
            print("Winner")
            break
        count+=1
        if count>3:
            print("Loser")
            break
        print("Guess Again")
        
guess_a_number()