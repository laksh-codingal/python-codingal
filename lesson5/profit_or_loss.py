
amount_spent_on_buying = float(input("enter the amount you spent on oranges:- "))
amount_made_on_selling = float(input("enter the amount you sold it for:- "))

if amount_made_on_selling>amount_spent_on_buying:
    profit = amount_made_on_selling - amount_spent_on_buying
    print("Good job! you made",profit,"profit on selling your oranges!!")
else:
    loss = amount_spent_on_buying - amount_made_on_selling
    print("you made", loss, "loss in selling your oranges..")

print("thank you")
