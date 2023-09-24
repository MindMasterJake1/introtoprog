# Task 1 - Hello World!

print("Hello, World!")  # Prints Hello World to the terminal

#Task 2 - Hello Name
# There are a few ways for the program to say the users name:
# Version 1 - Concatenation
name = "Jake"
print("Hello, "+name)

# Version 2 - print f function (More efficient).
name = "Jake"
print(f"Hello, {name}")

# Version 3 - Taking user input
name = input("Enter you name: ")
print(f"Hello, {name}")

#Version 4 - Preventing null values and errors using try / except
name = None
while not name:
    try:
        name = (input("Enter your name: "))
        valid = True
    except ValueError:
        print("Invalid input, make sure to enter a string")

# Task 3 - Celsius to Fahrenheit converter
Celsius = None
while not Celsius:
    try:
        Celsius = float(input("Enter the temperature in Celsius: "))
        Fahrenheit = (Celsius * 1.8) + 32
        print(f"The temperature of {Celsius}C, is {Fahrenheit}F")
    except ValueError:
        print("Please be sure to enter a number!")

#Task 4 - Batting average
matches_played = 609
batted = 1014
not_out = 106
runs = 48426
batting_average = runs / (batted - not_out)
print(f"Geoffery Boycott had a batting average of {batting_average}")

# Task 5 - PC Lab Problem
lab_group = 24
number_of_students = int(input("How many students are there? "))
number_of_groups = number_of_students // lab_group
left_over = number_of_students % lab_group
print(f"There will be {number_of_groups} groups, with {left_over} students left over")



