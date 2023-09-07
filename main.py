"""Module 1"""
"""Exersice 1
firstname = input("Enter your firstname please")
secondname = input("Enter your secondname please")
print("Hello, " + firstname + " " + secondname + "!")"""
"""Exersice 2
I did it"""
"""Module 2"""
"""Exersice 1
firstname = input("Enter your firstname please")
print("Hello, " + firstname + "!")"""
"""Exersice 2
radius = float(input("Enter a radius of a circle"))
area = float(2 * radius * radius)
print(area)"""
"""Exersice 3
length = float(input("Enter length of a rectangle please"))
width = float(input("Enter width of a rectangle please"))
perimeter = float(length + width)
area = float(length * width)
print(perimeter)
print(area)"""
"""Exersice 4
a = int(input("Enter first number please"))
b = int(input("Enter second number please"))
c = int(input("Enter third number please"))
sum = int(a + b + c)
product = int(a * b * c)
average = float((a + b + c) / 3)
print(f"sum: {sum} product: {product} average: {average:.2f}")"""
"""Exersice 5
talents = float(input("Enter mass in talents please"))
pounds = float(input("Enter mass in pounds please"))
lots = float(input("Enter mass in lots please"))
talentsintopounds = float(talents * 20)
poundsintolots = float((talentsintopounds + pounds) * 32)
lotsintograms = float((poundsintolots + lots) * 13.3)
kilograms = float(lotsintograms // 1000 )
grams = float(lotsintograms - (kilograms * 1000))
print(f"The weight in modern units: \n{kilograms:.0f} kilograms and {grams:.2f} grams.")"""
"""Exersice 6
I honestly don't know how to do it. We didn’t seem to take it to class, or I missed it :(."""
"""Module 3"""
"""Exersice 1
length = float(input("Enter length of a zander please"))
if length < 42:
    size = float(42-length)
    print(f"Release the fish back into the lake please. \nThe zander does not fulfill the size limit. Your zander is below the size limit by {size:.2f} centimeters.")
else:
    print("The zander is true to size. You caught a fish, congratulations!")"""
"""Exersice 2
cabin = input("Enter the cabin class of cruise ship please")
if cabin == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin == "A":
    print("Above the car deck, equipped with a window.")
elif cabin == "B":
    print("Windowless cabin above the car deck.")
elif cabin == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")"""
"""Exersice 3
gender = input("What is your biological gender? Male or Female")
value = float(input("What is your hemoglobin value (g/l)?"))
if gender == "Male":
    print("You are male.")
    if value < 134:
        print("Your hemoglobin is below average.")
    elif value >= 134 and value <= 167:
        print("Your hemoglobin value is normal.")
    elif value > 167:
        print("Your hemoglobin is above average.")
    else:
        print("You are not a male.")
if gender == "Female":
    print("You are female.")
    if value < 117:
        print("Your hemoglobin is below average.")
    elif value >= 117 and value <= 155:
        print("Your hemoglobin value is normal.")
    elif value > 155:
        print("Your hemoglobin is above average.")
    else:
        print("You are not a Female.")
if gender != "Male" and gender != "Female":
    print("Please write gender again.")"""
"""Exersice 4
year = float(input("Please enter year."))
if year % 4 == 0 and year % 100 != 0:
    print("The year is a leap year")
elif year % 100 == 0 and year % 400 == 0:
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")"""
#this is just a test
"""Module 2"""
"""Exersice 6
import random
symbols = str(input("Please write the number of symbols in the lock. Three or Four"))
if symbols == "Three":
    print(f"Your lock is: {random.randint(0,9):d}{random.randint(0,9):d}{random.randint(0,9):d}")
if symbols == "Four":
    print(f"Your lock is: {random.randint(1, 6):d}{random.randint(1, 6):d}{random.randint(1, 6):d}{random.randint(1, 6):d}")
if symbols != "Three" and symbols != "Four":
    print("Please select the number of symbols in the lock again.")
    print("Please select the number of symbols in the lock again.")"""
#  this is a test
"""Module 4"""
"""Exercise 1
a = 1
while a <= 1000:
    if a % 3 == 0:
        print(a)
        a += 1
    if a % 3 != 0:
        a += 1 """
"""Exercise 2
a = float(input("How many inches?"))
while a >= 0:
    a = a * 2.54
    print(f"It's {a} centimeters.")
    a = float(input("How many inches?"))"""
"""Exercise 3
list = []
a = input("Please write down a number.")
while a != '':
    if a == '':
        break
    if a != '':
        a = float(a)
        list.append(a)
    a = input("Please write down a number.")
if list:
    print(f"The smallest number is {min(list)}.")
    print(f"The largest number is {max(list)}.")
else:
    print("Please write at least one number.")"""
"""Exercise 4
import random
number = random.randint(1,10)
guess = int(input("Please guess the number between 1 and 10."))
while (number != guess):
    if number > guess:
        print("Too low")
        guess = int(input("Please guess the number between 1 and 10 again."))
    if number < guess:
        print("Too high")
        guess = int(input("Please guess the number between 1 and 10 again."))
else:
    print(f"Correct")"""
"""Exercise 5
a = 0
while a < 5:
    username = input("Please write down your username")
    password = input("Please write down your password")
    if username == "python" and password == "rules":
        break
    a += 1
if a == 5:
    print("Access denied")
else:
    print("Welcome")"""
"""Exercise 6
x = 1
y = 1
x_negative = -1
y_negative = -1
dots = int(input("How many dots?"))
a = int(0)
dotsin = int(0)
pi = float(0)
while a <= dots:
    import random
    X = random.uniform(x,x_negative)
    Y = random.uniform(y,y_negative)
    if X * X + Y * Y < 1:
        dotsin += 1
        a += 1
    else:
        a += 1
pi = 4 * dotsin / dots
print(pi)"""