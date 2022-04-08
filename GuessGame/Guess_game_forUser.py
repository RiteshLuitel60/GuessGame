import random
import os

os.system("cls")


def UserGuess():
    high = int(input("Highest limit for You to guess: "))
    guess_number = random.randint(0, high)
    guess_chance = 0
    # Condition
    
    while guess_chance < 3:
        user_guess = int(input("Enter your guess: "))
        guess_chance += 1
        
        if user_guess == guess_number:
            print(f"Correct. You Win! The secret number was {guess_number}. ")
            break
        elif user_guess > guess_number and guess_chance <= 2:
            print("Try Again and try lower")

        elif user_guess < guess_number and guess_chance <=2 :
            print("Try Again And try Higher")
            
        elif guess_chance == 3:
            print(f"you lost! The secret number was{guess_number}")

