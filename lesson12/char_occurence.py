
string = input("enter a string:- ")

char = input("enter a character:- ")

i = 0
count = 0
while i<len(string):

    if string[i]==char:
        count = count+1
    
    i = i+1

print(f'the character occured {count} times')

