import random

def play():
    user = input("Enter:'r' for Rock, 'p' for paper and 's' for scisors: ").lower()
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "its a tie"

    # r>s, s>p, p>r

    if iswin(user,computer):
        return "You won"

    return "You lost"

def iswin(player,opponent):

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())


    
