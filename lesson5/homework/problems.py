import random

# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.
# Create a list of 3 operating systems
operating_systems = ["Windows", "macOS", "Linux"]
print(operating_systems[len(operating_systems) - 1])
operating_systems.reverse()
print(operating_systems)


# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.
# Create a list of 4 school subjects
subjects = ["Math", "Science", "History", "English"]
print(subjects[1])
subjects.sort()
print(subjects)


# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then find the index of "403" and print it.
# Create a list of 5 error codes
error_codes = ["200", "301", "403", "404", "500"]
print(len(error_codes))
print(error_codes.index("403"))



# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
import random
languages = ["Python", "Java"]
print(random.choice(languages))
languages.append("C++")
print(languages)


# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
# Create a list of 6 passwords
passwords = ["alpha123", "beta456", "gamma789", "delta321", "omega654", "zeta987"]
middle_index = len(passwords) // 2
print(passwords[middle_index])
passwords.pop(0)
print(passwords)