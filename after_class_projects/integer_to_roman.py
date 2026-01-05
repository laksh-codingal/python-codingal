
def int_to_roman(num):
    
    integer = input("enter a number from 1 to 3999 only:- ")
    print(integer)
    if integer<1 and integer>3999:
        print("error, give number from 1 - 3999:- ")


    roman_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]
    
    result = []
    for value, symbol in roman_map:
        
        count, num = divmod(num, value)
        
        result.append(symbol * count)
        
        if num == 0:
            break

            
    return "".join(result)






