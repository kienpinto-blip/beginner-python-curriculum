# Problem 1
# Find and print the sum of all the numbers greater than 25 in the list.
numbers = [10, 32, 27, 8, 50]
total_sum = 0
for num in numbers:
    if num > 25:
        total_sum += num


# Problem 2
# Find and print the sum of all the numbers less than -10 in the list.
numbers = [-5, -20, -11, 0, 4, -15]
total_sum2 = 0
for num in numbers:
    if num < -10:
        total_sum2 += num



# Problem 3
# Find and print the biggest number less than 100 in the list.
numbers = [104, 99, 86, 120, 101]
under_100 = [num for num in numbers if num < 100]
if under_100:
    biggest_under_100 = max(under_100)
    print("The biggest number less than 100 is:", biggest_under_100)
else:
    print("There are no numbers less than 100 in the list.")
        
        

# Problem 4
# Find and print the biggest number in the list.
numbers = [12, 7, 33, 5]
biggest_number = max(numbers)
print("The biggest number in the list is:", biggest_number)
# Problem 5
# Find and print the total sum of all the numbers in the list.
numbers = [1, 3, 5, 7, 9]
total = numbers(1) + numbers(2) + numbers(3) + numbers(4) + numbers(5)
print(total)