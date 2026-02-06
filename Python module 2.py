#Question no 1

# Ask the fisher for the length of the zander in centimeters
length = float(input("Enter the length of the zander (cm): "))

# Size limit for a zander
size_limit = 42

# Check if the fish meets the size requirement
if length >= size_limit:
    print("The zander meets the size limit. You may keep the fish.")
else:
    difference = size_limit - length
    print("The zander is below the size limit.")
    print(f"Release the fish back into the lake.")
    print(f"It is {difference:.1f} cm below the size limit.")

#Question no 2

    # Ask the user to enter the cabin class
    cabin_class = input("Enter the cabin class (LUX, A, B, C): ").upper()

    # Check the cabin class and print the description
    if cabin_class == "LUX":
        print("Upper-deck cabin with a balcony.")
    elif cabin_class == "A":
        print("Above the car deck, equipped with a window.")
    elif cabin_class == "B":
        print("Windowless cabin above the car deck.")
    elif cabin_class == "C":
        print("Windowless cabin below the car deck.")
    else:
        print("Invalid cabin class.")

#Question no 3

# Ask for biological gender and hemoglobin value
gender = input("Enter biological gender (female/male): ").lower()
hemoglobin = float(input("Enter hemoglobin value (g/l): "))

# Check hemoglobin levels based on gender
if gender == "female":
    if hemoglobin < 117:
        print("Hemoglobin level is low.")
    elif hemoglobin <= 155:
        print("Hemoglobin level is normal.")
    else:
        print("Hemoglobin level is high.")

elif gender == "male":
    if hemoglobin < 134:
        print("Hemoglobin level is low.")
    elif hemoglobin <= 167:
        print("Hemoglobin level is normal.")
    else:
        print("Hemoglobin level is high.")

else:
    print("Invalid gender entered.")

#Question no 4

# Ask the user to enter a year
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")

