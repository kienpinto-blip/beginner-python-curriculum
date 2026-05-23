# Homework Problem 1
# Ask the user for two numbers.
# Print their quotient and remainder on separate lines.
number_one = int(input("Enter a number "))
number_two = int(input("Enter another number "))
print(number_one // number_two)
print(number_one % number_two)

# Homework Problem 2
# Ask the user for their favorite animal and favorite color.
# Print a sentence combining them like: "A blue tiger would be awesome!"
animal = input("Enter favorite animal ")
color = input("Enter favorite color ")
print("A", color, animal, "would be awsome!")
# Homework Problem 3
# Use a for loop to print all the even numbers from 0 to 10 (including 10)
for nums in range(0,11,2):
    print(nums)
# Homework Problem 4
# Ask the user how many push-ups they can do.
# Multiply it by 7 and print how many they could do in a week.
pushups_day = int(input("How much pushups can you do in a day? "))
print(pushups_day * 7)
# Homework Problem 5
# Use a for loop to print the square of each number from 1 to 6.
# (Example: 1*1=1, 2*2=4, etc.)
for nums in range(1, 7):
    print(nums * nums)