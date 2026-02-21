#QUESTION NO 1

number = 1

while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1


#QUESTION no 2

while True:
    inches = float(input("Enter inches (negative to quit): "))
    if inches < 0:
        break
    cm = inches * 2.54
    print(f"{inches} inches = {cm:.2f} cm")


#QUESTION NO 3

smallest = None
largest = None

while True:
    user_input = input("Enter a number (empty to quit): ")
    if user_input == "":
        break
    number = float(user_input)
    if smallest is None or number < smallest:
        smallest = number
    if largest is None or number > largest:
        largest = number

if smallest is not None:
    print(f"Smallest: {smallest}")
    print(f"Largest: {largest}")
else:
    print("No numbers were entered.")


#QUESTION NO 4

import random

secret = random.randint(1, 10)

while True:
    guess = int(input("Guess the number (1-10): "))
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct!")
        break


#QUESTION NO 5

attempts = 0

while attempts < 5:
    username = input("Enter username: ")
    password = input("Enter password: ")
    attempts += 1

    if username == "python" and password == "rules":
        print("Welcome")
        break
    else:
        print("Wrong credentials")

if attempts == 5 and not (username == "python" and password == "rules"):
    print("Access denied")


#QUESTION NO 6

import random


def approximate_pi(num_points):
    """Approximate pi using the Monte Carlo method."""
    inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 < 1:
            inside_circle += 1

    return 4 * inside_circle / num_points


def main():
    num_points = int(input("How many random points to generate? "))
    pi_estimate = approximate_pi(num_points)
    print(f"Approximation of pi with {num_points} points: {pi_estimate}")


if __name__ == "__main__":
    main()
