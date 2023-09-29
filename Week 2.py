# Practical Tasks
# Variable assignment
total = 100
print("The total is", total)
# total = total + 99
# print("The total is now", total)
# The above code is the same as:
total += 99
print("The total is now", total)
total -= 1
print("The total is", total)
total *= 4
print("The total is", total)
total /= 2
print("The total is", total)

total = 98.2
count = 5

average = (total + count) / 2
print("The average is", average)

# Data types
#False     Boolean
#1000      Integer
#100.111   Float
#"Hello"   String
#True      Boolean
# 100 / 5  Float
# 100 // 5 Integer

ans = "ABC" * 10
print(ans)

#Built-in functions
print("Jake")
print("Classified")
print("1234 567668")
print("My name is", len("Jake"), "letters long")

# The following will not work as the input operator always interoperates numbers as strings.
#age = input("Enter your age ")
#print("in one year your age will be", age + 1)


#Input form the user
age = input("Enter your age ")
age = int(age)
print("in one year your will be", age + 1)

number1 = int(input("Enter your first number to be multiplied: "))
number2 = int(input("Enter your second number to be multiplied: "))
product = number1 * number2
print(f"The product of the two numbers entered is {product}")

# Escape sequences:
print("This text includes characters such as \'\\\' and \"\'\",\n\tThis is a new line that strats with a tab\n\t\tThis new line starts with two tabs")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\nHello there!\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

# Triple quotes
print("""This text spans three lines
and includes both single ('),
and double quotes (")""")

#Indexing and slicing
surname = "Palin"
initial = surname[2]  # index always starts at 0
print(initial)
initial = surname[-2]
print(initial)

middle = surname[1:5]
print(middle)

last = surname[:-1]
print(last)

#lists
names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]
primes = [2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
slice_primes = primes[:4]
print(slice_primes)

names[5:5] = ["Mandy", "Bob"]
print(names)

nums = [1,2,3] * 5
print(nums)
