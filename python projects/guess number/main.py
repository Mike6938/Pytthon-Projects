# import random

# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f"guess a number between 1 and {x}: "))
#         print(f"wrong, your number is {guess}")
    
#     print(f"you are correct the number is {random_number}")

# guess(5)

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x}: "))
        if guess > random_number:
            print(f"sorry the number: {guess} is too high guess again")
            
        elif guess < random_number:
            print(f"sorry the number: {guess} is too low guess again")

    print(f"Hurrey , you have guessd the correct number {random_number}")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f'is {guess} too high(H), too low(L), or correct (c) ').lower()
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1
    print(f'yay! the computer guessed your number, {guess}, corectly')

computer_guess(100)
guess(5) 



