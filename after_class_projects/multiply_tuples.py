
try:
    tuplee = input("enter a tuple like this (1, 2, 3):- ")

except:
    print("enter a tuple like this (1, 3, 4):- ")


numbers = eval(tuplee)

result = 1
for num in numbers:
    result *= num

print("The product of all tuple numbers is:- ", result)
