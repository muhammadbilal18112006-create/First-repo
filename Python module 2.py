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