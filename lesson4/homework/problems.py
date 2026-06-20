# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."
test_score1 = int(input("enter a test score "))
test_score2 = int(input("enter anouther one"))
if test_score1 and test_score2 < 50:
    print("you passed both tests! ")
else:
    print("You falled at least one")
# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."
lunch = input("Did you bring lunch? ")
water = input("Did you bring water")
if lunch and water == "Yes":
    print("You are prepared")
elif lunch == "Yes" and water == "No":
    print("You are somewhat ready")
elif water == "Yes" and lunch == "No":
    print("You are somewhat ready")
else:
    print("You are not ready")
# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."
number_range = input("Enter a number")
if number_range is not range (1,10):
    print("Out of range")
else:
    print("In range")
# Problem 4
# Generate a random number between 1 and 10.
# Ask the user to guess.
# If the guess is right AND the number is even, print "Even match!"
# Else if guess is right OR number is 5, print "Nice try!"
# Otherwise, print "Nope."
import random
secret_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
if guess == secret_number and secret_number % 2 == 0:
    print("Even match!")
elif guess == secret_number or secret_number == 5:
    print("Nice try!")
else:
    print("Nope.")


# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."
import random
secret_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
if guess == secret_number and secret_number % 2 == 0:
    print("Even match!")
elif guess == secret_number or secret_number == 5:
    print("Nice try!")
else:
    print("Nope.")