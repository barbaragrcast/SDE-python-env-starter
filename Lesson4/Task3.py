import random

number = random.randint(1, 10)
print("Hello, welcome to the number guessing game.")

def game():
    guess = input("Please guess a number between 1-10 ")
    if int(guess) == number:
        print('congrats! you guess it')
    else:
        print("Sorry, that was not the number. Try again!")
        game()
game()