
choice = input("do you want to find the perimetre of a square or retangle:- ")
if choice == "square":
    lenghts = int(input("enter a lenght of a side:- "))
    lenghts2 = int(input("enter a lenght of a side:- "))
    lenghts3 = int(input("enter a lenght of a side:- "))
    lenghts4 = int(input("enter a lenght of a side:- "))
    def square():
        perimiter = lenghts+lenghts2+lenghts3+lenghts4
        print(perimiter)
    square()

elif choice == "rectangle":
    lenghts1 = int(input("enter a lenght of a side:- "))
    lenghts22 = int(input("enter a lenght of a side:- "))
    def rectangle():
        perimiter1 = (lenghts1 + lenghts22)*2
        print(perimiter1)
    rectangle()

else:
    print("invalid input!")






