vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.append("carrots")#the task said to add an item
vegetables.remove("onions")#the task said to remove the 2one index
vegetables.append("cucumbers")#the task said to add an item

if "carrots" not in vegetables:
    vegetables.appened("carrots")
else:
    print("Carrots are already in the list.")

if "cucumbers" not in vegetables:
    vegetables.appened("cucumbers")
else:
    print("Cucumbers are already in the list.")
    

vegetables.sort()
print("Updated Vegetable Inventory:", vegetables)