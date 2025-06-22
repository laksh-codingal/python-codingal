
import random

playing = True
number = str(random.randint(1,20))

print("i will generate a number from 1 to 20 try and guess it!!")

while playing:
    guess = (input("enter your best guess:- "))
    if guess == number:
        print("you guessed it!!")
        print("the number was", number)
        break

    else:
        print("try again")

