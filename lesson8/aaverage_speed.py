cycle1 = input("enter the name of your cycle:- ")
cycle1_speed = int(input(f"enter the speed of your {cycle1}:- "))
cycle2 = input("enter the name of your cycle:- ")
cycle2_speed = int(input(f"enter the speed of your {cycle2}:- "))
cycle3 = input("enter the name of your cycle:- ")
cycle3_speed = int(input(f"enter the speed of your {cycle3}:- "))

average = (cycle1_speed + cycle2_speed + cycle3_speed) / 3
print(average)
if average > cycle1_speed and average>cycle2_speed and average>cycle3_speed:
    print(f"{average} is higher than {cycle1_speed}, {cycle2_speed}, {cycle3_speed}")
elif average>cycle1_speed and average>cycle2_speed:
    print(f"{average}, is higher than {cycle1_speed}, {cycle2_speed}")
elif average>cycle1_speed and average>cycle3_speed:
    print(f"{average} is higher than {cycle1_speed}, {cycle3_speed}")
elif average>cycle2_speed and average>cycle3_speed:
    print(f"{average} is higher than {cycle2_speed}, {cycle3_speed}")
elif average>cycle1_speed:
    print(f"{average} is higher than {cycle1_speed}")
elif average>cycle2_speed:
    print(f"{average} is higher than {cycle2_speed}")
elif average>cycle3_speed:
    print(f"{average} is higher than {cycle3_speed}")
else:
    print("invalid input")
