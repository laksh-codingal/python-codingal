
def tip(bill,tip_percentage):
    total = bill * (1+0.01 * tip_percentage)
    total = round(total,2)
    print(total)
bill = float(input("ENTER YOUR BILL:- "))
tip_percentage = float(input("ENTER YOUR TIP PERCENTAGE:- "))
    
tip(bill,tip_percentage)