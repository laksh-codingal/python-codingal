
string = input("enter a string to be reversed:- ")
string2 = ''
for i in string:
    string2 = i+string2
print(f'the original string is {string}')
print(f'the reversed string is {string2}')
