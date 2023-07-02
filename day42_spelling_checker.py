from textblob import TextBlob
def spelling_checker():
    
    word = TextBlob(input("enter any word: "))
    
    suggest = word.correct()
    
    if word == suggest:
        return word
    
#     print(f"do you mean {suggest} ?")
    userInput = input(f"do you mean {suggest} ?: ") 
    if userInput == "no":
        word = TextBlob(input("enter any word: "))
        suggest = word.correct()
        return suggest
        
    if userInput == "yes":
        suggest = word.correct()
        return suggest
    
print(spelling_checker())