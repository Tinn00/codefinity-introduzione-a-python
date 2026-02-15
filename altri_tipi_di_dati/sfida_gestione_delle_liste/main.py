#create a list
meat = ["Ham", 3.99, 50, "Sliced"] #product, price, quantity, type
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]

#create the main list
deli_dept = [meat, cheese, condiment]

#restock the item
if "Ham" in meat and meat[2] <100: 
    meat[2] = 100

#add seasonal meat
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)

#remove condiment
deli_dept.remove(condiment)

#sort the list
deli_dept.sort()
print("Initial Deli List:", deli_dept)
print("Updated Deli List:", deli_dept)

#Personal Note: Until now, I used AI, but with this code I started learning how to add parameters by myself and understand the logic of programming