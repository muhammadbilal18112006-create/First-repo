#Question no 1

import random

# function that returns a random dice roll between 1 and 6
def roll_dice():
    return random.randint(1, 6)


# main program
result = 0

while result != 6:
    result = roll_dice()
    print("Dice rolled:", result)


#Question no 2

import random

# function that returns a random dice roll
# sides = number of sides on the dice
def roll_dice(sides):
    return random.randint(1, sides)


# main program

# ask user how many sides the dice has
max_number = int(input("Enter number of sides on the dice: "))

result = 0

# keep rolling until we get the maximum number
while result != max_number:
    result = roll_dice(max_number)
    print("Dice rolled:", result)

#Question no 3

# function to convert gallons to litres
def gallons_to_litres(gallons):
    litres = gallons * 3.785   # 1 US gallon = 3.785 litres
    return litres


# main program
while True:
    gallons = float(input("Enter gasoline amount in gallons (negative number to stop): "))

    # stop if user enters negative value
    if gallons < 0:
        break

    litres = gallons_to_litres(gallons)
    print("Litres:", litres)

#Question no 4

# function that returns the sum of numbers in a list
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total


# main program

# create a list of integers
my_list = [5, 10, 15, 20]

# call the function
result = sum_of_list(my_list)

# print the result
print("Sum of the list is:", result)

#Question no 5

# function that removes uneven (odd) numbers from a list
def remove_uneven_numbers(numbers):
    new_list = []

    for num in numbers:
        if num % 2 == 0:   # keep only even numbers
            new_list.append(num)

    return new_list


# main program

# create a list of integers
original_list = [1, 2, 3, 4, 5, 6, 7, 8]

# call the function
even_list = remove_uneven_numbers(original_list)

# print both lists
print("Original list:", original_list)
print("List without uneven numbers:", even_list)


#Question no 6

import math

# function to calculate unit price (euros per square meter)
def pizza_unit_price(diameter_cm, price_euro):
    # convert diameter from cm to meters and find radius
    radius_m = (diameter_cm / 100) / 2

    # calculate area of pizza (circle area = pi * r^2)
    area = math.pi * (radius_m ** 2)

    # unit price = price divided by area
    unit_price = price_euro / area
    return unit_price


# main program

# input for pizza 1
diameter1 = float(input("Enter diameter of pizza 1 (cm): "))
price1 = float(input("Enter price of pizza 1 (euros): "))

# input for pizza 2
diameter2 = float(input("Enter diameter of pizza 2 (cm): "))
price2 = float(input("Enter price of pizza 2 (euros): "))

# calculate unit prices using the function
unit1 = pizza_unit_price(diameter1, price1)
unit2 = pizza_unit_price(diameter2, price2)

# print unit prices
print("Pizza 1 unit price (€/m^2):", unit1)
print("Pizza 2 unit price (€/m^2):", unit2)

# compare which is better value
if unit1 < unit2:
    print("Pizza 1 provides better value for money.")
elif unit2 < unit1:
    print("Pizza 2 provides better value for money.")
else:
    print("Both pizzas have the same value.")




