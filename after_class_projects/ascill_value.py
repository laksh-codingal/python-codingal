
char = input("enter a character:- ")

if len(char) == 1:

    acsil_value = ord(char)
    print(f"the ACSIL value of {char} is {acsil_value}")
else:
    print("please enter only a single character")
    