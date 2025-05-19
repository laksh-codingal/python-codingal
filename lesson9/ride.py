
print("select your ride")
print("1. car"
      " 2. bike")
ride = int(input("enter your choice:- "))
if ride == 1:
    print("choose your type:-" \
    "1. sedan " \
    " 2. suv")
    choice1 = int(input("enter your tyep:- "))
    if choice1 == 1:
        print("enjoy the ride in a sedan")
    elif choice1 == 2:
        print("enjoy the ride in a suv")
    else:
        print("invalid input")

elif ride == 2:
    print("choose your type:-" \
    "1. sport" \
    " 2. scooty")
    choice2 = int(input("enter your tyep:- "))
    if choice2 == 1:
        print("enjoy the ride in a sport bike")
    elif choice2 == 2:
        print("enjoy the ride in a scooty")
    else:
        print("invalid input")
else:
    print("invalid input")
