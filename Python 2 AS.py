#QUESTION NO 1

name = input("Enter your name: ")
print(f"Hello, {name}!")


#QUESTION NO 2

import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print(f"The area of the circle is {area:.2f}")


#QUESTION NO 3

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

perimeter = 2 * (length + width)
area = length * width

print(f"The perimeter of the rectangle is {perimeter:.2f}")
print(f"The area of the rectangle is {area:.2f}")

#QUESTION NO 4

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

total = num1 + num2 + num3
product = num1 * num2 * num3
average = total / 3

print(f"Sum: {total}")
print(f"Product: {product}")
print(f"Average: {average:.2f}")


#QUESTION NO 5

Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti). The program converts the input to full kilograms and grams and outputs the result to the user:

One talent is 20 pounds.
One pound is 32 lots.
One lot is 13,3 grams.
Example output:

Enter talents:
3

Enter pounds:
9

Enter lots:
13.5

The weight in modern units:
29 kilograms and 545.95 grams.