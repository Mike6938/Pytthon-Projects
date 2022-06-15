import random
import string
from words import words

def get_valid_words(words):
    word = random.choice(words) 
    while '_' in word or '' in word:
        word = random.choice(words)

    return word

def hangman():
    lives = 6
    word = get_valid_words(words)
    word_letters =set(words) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed
 
    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #letters used
        #''.join(['a','b','cd']) --> 'a b cd'
        print('you have', lives,'left and you have used this letters: ' ' '.join(used_letters))

        #what current word is (ie w-rd)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word: ', ''.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print('the letter you guessed is not in the word')

        elif user_letter in used_letters:
            print('you have already used that character. please try again')

        else:
            print('invalid character. please try again.')

    if lives == 0:
        print('Game over, the word is:',word)
            
    else:
        print('You Won!!!! the word is:', word)

hangman()
