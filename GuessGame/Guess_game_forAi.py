import random
import os

os.system("cls")

def computerGuess():
    
    # high is the uppeer limit of the number for computer to guess
     
    high = int(input("Highest limit for computer to guess: "))
    
    low = int(input("lowest limit for the computer to guess your number: "))
    
    # random number in your mind that you want computer to guess
    secret_number = int(input("What you want computer to guess: "))
    
    # guess_chance is used to give ai the number of tries
    guess_chance = 0
    
    computer_guess = int()
    
    while guess_chance < 10 and secret_number != computer_guess:
        
        computer_guess = random.randint(low, high)
        
        guess_chance += 1           
            
    
        # elif secret_number > high:
        #     print("Error! your number is greater than the maximum value. ")    
    
        
        if computer_guess < secret_number and guess_chance < 10  and computer_guess != secret_number:
        
            print(f"Ai tried { computer_guess} ")
            low = computer_guess + 1        
            

        
        elif computer_guess > secret_number and guess_chance < 10 and computer_guess != secret_number :
            print(f"AI TRIED { computer_guess} ")
            high = computer_guess - 1
            
        
        elif guess_chance == 10:
            print("computer couldn't guess your number. 😢")
    
    print(f"AI Guessed your secret number {secret_number} correctly in {guess_chance} tries. ")        
             
            
computerGuess()
        
        
