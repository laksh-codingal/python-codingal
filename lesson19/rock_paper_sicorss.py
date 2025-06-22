
import random

choice = random.choice(["rock", "paper", "scissors"])

user_choice = input("enter your choice:- ")

if choice == user_choice:
    print("its a tie!!")

elif user_choice == "rock" and choice == "paper":
    print("you lose!")

elif user_choice == "rock" and choice == "scissors":
    print("you win!!")

elif user_choice == "paper" and choice == "scissors":
    print("you lose!")

elif user_choice == "paper" and choice == "rock":
    print("you win!!")

elif user_choice == "scissors" and choice == "rock":
    print("you lose!")

elif user_choice == "scissors" and choice == "paper":
    print("you win!!")

else:
    print("invalid input!")

