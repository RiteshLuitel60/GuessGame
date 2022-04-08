import random
import os

os.system("cls")


def engaging_Ai_guessGame():
    
    low = 1
    high = int( input("your upper limit for the guess: ") )
    
    ask_user = ''
    
    while ask_user != 'c' :
        
        
        if low != high:
            Ai_guess = random.randint(low, high)
            
        else:
            Ai_guess = high # could be anything either high or low because both variable have the same value
            
        ask_user = input(f"is {Ai_guess} 'C' if correct, 'H' high if too high and 'L' if too low: ").lower()
        
            
        
        if ask_user == "h":
            high = Ai_guess - 1

            
        elif ask_user == "l":
            low = Ai_guess + 1
            
        if high == low: 
            print(f"your secret number is {high}" )
            break

    if ask_user == "c":
        print(f"wow! AI guessed your number, {Ai_guess}, correctly!")
            
     
engaging_Ai_guessGame()
