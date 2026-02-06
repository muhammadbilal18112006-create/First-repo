#Question no 1

import random

# Ask the user how many dice to roll
number_of_dice = int(input("How many dice to roll? "))

total = 0

# Roll the dice using a for loop
for i in range(number_of_dice):
    roll = random.randint(1, 6)  # simulate rolling one die
    total += roll

# Print the sum of the dice
print("Sum of the dice:", total)

#Question no 2


# Create an empty list to store numbers
numbers = []

# Ask the user to enter numbers until an empty string is given
while True:
    user_input = input("Enter a number (press Enter to quit): ")

    if user_input == "":
        break

    number = float(user_input)
    numbers.append(number)

# Sort the numbers in descending order
numbers.sort(reverse=True)

# Get the five greatest numbers
top_five = numbers[:5]

# Print the result
print("The five greatest numbers are:")
for num in top_five:
    print(num)

#Question no 3

# Ask the user for an integer
number = int(input("Enter an integer: "))

# Check if the number is a prime number
if number <= 1:
    print("The number is not a prime number.")
else:
    is_prime = True

    # Check divisibility from 2 up to number-1
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("The number is a prime number.")
    else:
        print("The number is not a prime number.")

#Question no 4

# Create an empty list to store city names
cities = []

# Ask the user to enter five city names
for i in range(5):
    city = input(f"Enter the name of city {i+1}: ")
    cities.append(city)

# Print the city names one by one
print("\nCities entered:")
for city in cities:
    print(city)
