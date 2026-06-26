# Problem 1
# Count and print how many times "Alex" appears in the list.
names = ["Liam", "Alex", "Sophie", "Alex", "Mia"]
alex_count = names.count ("Alex")
print(alex_count)
# Problem 2
# Search for "elephant" in the list and print if it's found.
animals = ["zebra", "giraffe", "lion", "tiger"]
if "elephant" in animals:
    print("Elephant is in animals")
else:
    print("Elephant is not found")
# Problem 3
# Count and print how many scores are 100.
scores = [95, 100, 88, 100, 77, 92]
score_count = scores.count(100)
print(score_count)
# Problem 4
# Search for the color "blue" in the list and print its index if it's found.
colors = ["red", "green", "blue", "yellow"]
if "blue" in colors:
    print("Blue is in colors")
# Problem 5
# Count and print how many temperatures in the list are below zero.
temperatures = [3, -2, 5, -7, 0, 4, -1]

count = 0
for temp in temperatures:
    if temp < 0:
        count += 1

print(count)