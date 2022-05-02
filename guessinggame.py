import random

guessingGame = int(input('Guess the number between 1 and 9'))

number = random.randrange(1,9)

while chances < 5:

if guess == number:
    print("Congrats You Won")
    break

if not chances < 5:
    print("You loss, the number is", number)
    


