menu = ["Coffee", "Tea", "Biscuits", "Pizza"]
stock = { 
    "Coffee": 10,
    "Tea": 30,
    "Biscuits": 40,
    "Pizza": 2
}


price = { 
    "Coffee": 1.20,
    "Tea": 1.10,
    "Biscuits": 3.10,
    "Pizza": 10.10
}

total_stock = 0
for x in stock:
    total_stock += stock[x] * price[x]

print(total_stock)

