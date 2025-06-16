
def factorial(num):
    '''this is a recursive function to find the factorial of a number'''
    if num == 0 or num == 1:
        return 1 
    
    else:
        return num * factorial(num-1)

print(factorial.__doc__)
print(factorial(999))
print(factorial(999))
print(factorial(999))
print(factorial(999))

