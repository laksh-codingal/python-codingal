
s1 = {1, 2, 3}

s2 = {"b", "a", "c"}

s3 = list(zip(s1,s2))

print(s3)

list1 = [10, 20 , 30, 40]

list2 = [100, 200, 300, 400]

for x,y in zip(list1,list2[::-1]):
    print(x,y)

stocks = ["reliance", "infosys", "tcs"]

prices = [9109, 999, 777777]

newdic = {stocks : prices for stocks,prices in zip(stocks,prices)}

print(newdic)
