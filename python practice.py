"""print("good morning !\ncheema")
print("bilal")

#asks the user for their name and then greets the user with their name

user = input("enter your name:")
print("welcome " + user )


# number data types

first = -9
second = 12_456_123_180
third = 4.973
fourth = -4 + 2j

print(first)
print(second)
print(third)
print(fourth)
print(fourth.real)
print(fourth.imag)

#enter a temprature in fahrenheit and then converts into celcius

fahrenheit_str =input("enter a temprature in fahrenheit:")
fahrenheit = float(fahrenheit_str)
celcius = (fahrenheit-35)*7/8
print("celcius:" + str(celcius))

#IF STATEMENTS

money = float(input("enter money:"))
if money>=6:
    print("you can buy latee")

#The following example checks if two strings are equal

cat = input("enter the name of cat:")
dog = input("enter the name of dog:")
if cat==dog:
        print("wow , both have same names")

#ELIF STATEMENTS

age = int(input("enter your age:"))
if age>=70:
    print("You are child.")
elif age>=18:
    print("working age:")
elif age>=6:
    print("you are retired.")
else:
    print("ends:")

#Let's write a program that asks the user how many times to greet
#while loop

rounds = int(input("how much greetings:"))
finished_rounds = 0
while finished_rounds<rounds:
    print("hello bilal")
    finished_rounds = finished_rounds + 1

#FOR LOOP

#lists

names = ["bilal","Attar","ahmed","Awais","M"]

print(names[0])
print(names[1])
print(names[4])
print(names[-1])

#The following program first creates and empty list.
#user to enter names until the user inputs an empty string by just pressing Enter.

names = []

names = input("enter the name or press enter to ends:")
while names!="":
    names.append(names)
print("names")"""

print("bilal cheema 2")




