
import random

score = 0 
num_of_questions = int(input("enter the number of questions:- "))
def questions():
    global score
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'what is {num1} + {num2}'
    correct_answer = num1 + num2

    print(question)
    try:
        user_answer = int(input("enter answer:- "))
    except:
        print("error")

    if user_answer == correct_answer:
        score += 1
    else:
        pass


for i in range(num_of_questions):
    questions()

print(f"you got {score} out of {num_of_questions} correct.")
