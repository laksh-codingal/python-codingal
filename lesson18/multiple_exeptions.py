
try:
    num1,num2 = eval(input("enter 2 numbers seperated with a comma. eg:- 1,2:- "))
    result = num1/num2
    print(result)

except ZeroDivisionError:
    print("you cannot give zero as num2 because its an error")

except SyntaxError:
    print("there is a syntax error maybe try seperating the numbers with a comma")

except:
    print("wrong input")

else:
    print("there is no exceptions")

finally:
    print("bye")
    
