
import random

class fruitquiz:

    def __init__(self):
        self.fruits = {
            "apple":"red",
            "orange":"orange",
            "grapes":"green",
            "banana":"yellow"
        }

    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            print("what is the color of", fruit)
            answer = input()
            if answer.lower()== color:
                print("correct answer")

            else:
                print("wrong answer")
            option = int(input("enter 0 to continue or else 1 to exit"))
            if option:
                break

print("welcome to the fruit quiz")
fq = fruitquiz()
fq.quiz()

