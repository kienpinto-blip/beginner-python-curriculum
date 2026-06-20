# Problem 1
# Ask the user to enter a number.
# Print "Even" if the number is divisible by 2, otherwise print "Odd".
nums = int(input("Enter a number"))
if nums % 2 == 0:
    print("Even")
else:
    print("Odd")
# Problem 2
# Ask the user for the day of the week (all lowercase).
# Print "Weekend" if the day is "saturday" or "sunday",
# else print "Weekday".
day = input("What is the day ")
if day == "saturday" or "sunday":
    print("It is the weekend")
else:
    print("It is the weekday")


# Problem 3
# Generate a random number between 1 and 10 (inclusive).
# Ask the user to guess the number.
# Print "Correct!" if the guess matches the random number, else print "Try again!".
import random
guess_number = random.randint(0,10)
number = int(input("Enter a number"))
if number == guess_number:
    print("You got the right number")
else:
    print("You got the number ")

# Problem 4
# Ask the user for a positive integer.
# If the number is divisible by 2 and greater than 10, print "Big even number".
# Otherwise print "Number does not meet criteria".
numb = input("Enter a number ")
if numb > 10 and numb % 2 == 0:
    print("Big even number")
else:
    print("Number does not meet criteria")

# Problem 5
# Ask the user for two numbers.
# Print which number is larger.
# If the numbers are equal, print "Numbers are equal".
number_1 = input("Enter a number ")
number_2 = input("Enter a next number ")
if number_1 > number_2:
    print(number_1)
elif number_2 > number_1:
    print(number_2)
else:
    print("Numbers are equal")