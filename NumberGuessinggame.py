# import random
# number = random.randrange(1,100)
# guess = 0

# while guess != number:
    
#     guess = int(input("Enter Guess: "))
    
#     if (guess < number):
#         print("Guess higher!")
#     elif (guess > number):
#         print("Guess lower!") 
#     else:
#         print("You won!")

import random


secret_number = random.randint(1, 100)


max_attempts = 3
attempts = 0

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    attempts += 1

    if guess < secret_number:
        print("Try a higher number.")
    elif guess > secret_number:
        print("Try a lower number.")
    else:
        print(f"Congratulations! You've guessed the secret number {secret_number} in {attempts} attempts!")
        break

if attempts == max_attempts:
    print(f"Sorry, you've used all {max_attempts} attempts. The secret number was {secret_number}. Better luck next time!")