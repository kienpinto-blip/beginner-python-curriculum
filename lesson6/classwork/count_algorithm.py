animals = ["whale", "tiger", "crocodile", "tiger", "monkey"]
print(animals)

# You can use built-in Pyton funcions to cout item
num_tiger = animals.count("tiger")
print("There are", num_tiger, "tigers")

print("Our algorithem is; ")

counter = 0
for i in range(len(animals)): # This code goes through each item in the list.
    item = animals[i]
    if item == "tiger": # Checks if the item is "tiger".
        counter = counter + 1 # If the item is "tiger" add one more to the counter.
print(counter, "tigers")

numbers = [14, 1, 50, 4, 20, 12]
counter = 0
for i in range(len(numbers)):
    item = numbers[i]
    if item > 10:
        counter = counter + 1
print(counter, "numbers above 10")