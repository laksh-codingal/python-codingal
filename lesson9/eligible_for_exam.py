
medical_cause = input("do you have a medical cause?. enter Y or N:- ")
attendance = int(input("enter your attendence:- "))

if medical_cause == "Y":
    print("you can write the exam")
else:
    if attendance >= 75:
        print("you can write the exam")
    else:
        print("you cannot write the exam")
