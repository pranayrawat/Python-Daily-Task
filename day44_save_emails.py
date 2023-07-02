def save_emails():

    with open('emails.csv','w') as file:
        
        while True:
            userInput = input("email: ")
            file.write(userInput+'\n')
            
            done = input("are you done ?(y/n): ")
            if done == 'y':
                break

def open_emails():
    with open('emails.csv','r') as readFile:
        print(readFile.read())

save_emails()
open_emails()

