inventory = {
    "Rice": 50,
    "Sugar": 40,
    "Bread": 30,
    "Milk": 25,
    "Tea": 20
}

print("Quantity of Rice:", inventory["Rice"])

inventory["Soap"] = 35
inventory["Sugar"] = 45
inventory.pop("Bread")

print("Final Inventory:", inventory)
