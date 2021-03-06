import random
import os

os.system("cls")

# os is imported to avoid unnecessary lines while running the code in vs code Terminal.

def computerGuess():
    
    # high is the upper limit of the number for computer to guess
     
    high = int(input("Highest limit for computer to guess: "))
    
    low = int(input("lowest limit for the computer to guess your number: "))
    
    # random number in your mind that you want computer to guess
    secret_number = int(input("What you want computer to guess: "))
    
    # guess_chance is used to give computer the number of tries 
    guess_chance = 0
    
    computer_guess = int()
    
    while guess_chance < 10 and secret_number != computer_guess:
        
        computer_guess = random.randint(low, high)
        
        guess_chance += 1           
        
        # useless line of code line 31 and 32    
        # elif secret_number > high:
        #     print("Error! your number is greater than the maximum value. ")    
        
    
        # Below line of code sets new value of "low" variable to narrow domn the numbers to guess the correct one.
        if computer_guess < secret_number and guess_chance < 10  and computer_guess != secret_number:
        
            print(f"Ai tried { computer_guess} ")
            low = computer_guess + 1        
            

        # Below line of code sets new value of "high" variable to narrow domn the numbers to guess the correct one.
        elif computer_guess > secret_number and guess_chance < 10 and computer_guess != secret_number :
            print(f"AI TRIED { computer_guess} ")
            high = computer_guess - 1
            
        # line 47 prints sorry message if computer couldn't guess the secret number wihtin 10 tries.
        elif guess_chance == 10:
            print("computer couldn't guess your number. 😢")
    
    print(f"AI Guessed your secret number {secret_number} correctly in {guess_chance} tries. ")        
             
            
computerGuess()
        
        
