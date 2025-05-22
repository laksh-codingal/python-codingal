
num = int(input("Enter the a number:- "))
power = int(input("Enter the power:- "))

result = 1
for _ in range(power):
    result *= num

print(f"{num} to the power of {power} is {result}")
