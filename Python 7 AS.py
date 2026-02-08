#Question no 1

# tuple containing seasons
seasons = ("winter", "spring", "summer", "autumn")

# ask user for month number
month = int(input("Enter month number (1-12): "))

# check season based on month
if month == 12 or month == 1 or month == 2:
    season = seasons[0]   # winter
elif month == 3 or month == 4 or month == 5:
    season = seasons[1]   # spring
elif month == 6 or month == 7 or month == 8:
    season = seasons[2]   # summer
elif month == 9 or month == 10 or month == 11:
    season = seasons[3]   # autumn
else:
    season = "invalid month"

print("Season is:", season)


#Question no 2

# create an empty set to store names
names = set()

while True:
    # ask user to enter a name
    name = input("Enter a name (empty to stop): ")

    # stop if empty string
    if name == "":
        break

    # check if name already exists
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

# print all names
print("\nNames entered:")
for n in names:
    print(n)


#Question no 3

# dictionary to store airport data
# key = ICAO code, value = airport name
airports = {}

while True:
    print("\nChoose an option:")
    print("1 = Enter a new airport")
    print("2 = Fetch airport information")
    print("3 = Quit")

    choice = input("Your choice: ")

    # option 1: add new airport
    if choice == "1":
        icao = input("Enter ICAO code: ").upper()
        name = input("Enter airport name: ")
        airports[icao] = name
        print("Airport added.")

    # option 2: fetch airport info
    elif choice == "2":
        icao = input("Enter ICAO code to search: ").upper()
        if icao in airports:
            print("Airport name:", airports[icao])
        else:
            print("Airport not found.")

    # option 3: quit program
    elif choice == "3":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Try again.")


