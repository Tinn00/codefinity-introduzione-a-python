# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

#Count how many times 'apples' are on the shelf.
apple_count = shelf.count("apples")
print("Number of Apples:", apple_count)

#Find the index of the first occurrence of bananas
banana_index = shelf.index("bananas")
print("First Banana Index:", banana_index)

#Check if apples need to be restocked
if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")

#Check if grapes need to be restocked (if grapes appear only once)
grape_count = shelf.count("grapes")
if grape_count == 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")

#Check if oranges are on the shelf and print their index or stock status
oranges_index = shelf.index("oranges")
if "oranges" in shelf:
    print("Oranges are at index:", oranges_index)
else:
    print("Oranges are out of stock.")