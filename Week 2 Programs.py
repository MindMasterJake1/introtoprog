#Week 2 Programs

#Task 1 - Greeting
name = input("Hello, what is your name? ")
print(f"Hello, {name}. Good to meet you!")

#Task 2 - C to F version 2
Celsius = None
while not Celsius:
    try:
        Celsius = float(input("Enter a temperature in Celsius: "))
        Fahrenheit = (Celsius * 1.8) + 32
        print(f"{Celsius}C, is equivalent to {Fahrenheit}F.")
    except ValueError:
        print("Please be sure to enter a number!")

#Task 3 - PC Lab Problem Version 2
number_of_students = int(input("How many students are there? "))
lab_group = int(input("Required group size? "))
number_of_groups = number_of_students // lab_group
left_over = number_of_students % lab_group
if left_over == 1:
    print(f"There will be {number_of_groups} groups, with {left_over} student left over")
elif left_over == 0:
    print(f"There will be {number_of_groups} groups, with no students left over")
else:
    print(f"There will be {number_of_groups} groups, with {left_over} students left over")

# Task 4 - Sweet distribution
sweets = int(input("How many sweets do you have? "))
students = int(input("How many students are there? "))

per_student = sweets // students
print(f"Each pupil will receive {per_student} sweets")
