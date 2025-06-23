
def hotel_cost(nights):
    return nights * 700

def plane_cost(city):
    if city == "chennai":
        return 770
    elif city == "bangalore":
        return 880
    elif city == "hosur":
        return 200
    elif city == "kanyakumari":
        return 1000
    
def rental_cost(days):
    if days>=7:
        return 40*days - 50
    elif days>=3:
        return 40*days - 20
    else:
        return 40 * days
    
def trip_cost(city,days,spending_money):
    return rental_cost(days) + hotel_cost(days) + plane_cost(city) + spending_money

print("cost of car_rental is ",rental_cost(7))
print("the cost of plane is", plane_cost("chennai"))
print("hotet room is", hotel_cost(7))
print("the total amount spent on the trip is", trip_cost("chennai",7,7000))
