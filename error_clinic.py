#Lab 5, Bao Pham, Error Clinic

#Snippet 1

#PREDICT; If y = 0, this block of code will give out a ZeroDivision Error.

x = 10
y = 1
result = x / y
print("Result: ", result)

#Snippet 2

#PREDICT; I feel like this block would give out a TypeError, as it doesn't make sense to add 1 to an index.

numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print(numbers[i+0])

#Snippet 3

#PREDICT; There is a missing colon in this definition, so it is a Syntax error.

def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area

radius = 5
print(calculate_area(radius))

#Snippet 4

#PREDICT; Also missing the two colons for the if/else statement, Syntax error.

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(4))
print(is_even(7))

#Snippet 5

#PREDICT; Another missing colon, Syntax error.

for i in range(5):
    print(i)

#Snippet 6

#PREDICT; For this block, you need a comma to link variables in an expression, otherwise Syntax error.

def greet(name):
    return "Hello, ", name
print(greet("Alice"))

#Snippet 7

#PREDICT; The functionality of the for loop isn't indented, leading to an IndentError.

numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total += number
print("Sum of numbers: ", total)

#Snippet 8

#PREDICT; I feel like you need to switch places for the if/else statements in order for it to work?

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

#Snippet 9

#PREDICT; I think the "or" causes the if statement to look for any string, even if it doesn't fit the exact name.

name = input("Enter your name: ")
if name == "Alice" or name == "Bob":
    print("Hello, " + name)
else:
    print("Hello, stranger!")

#Snippet 10

#PREDICT; There needs to be a failsafe in order for 0 to be accepted as an answer logically, otherwise its a ZeroDivisionError.

def divide_numbers(x, y):
    
    if x >= 1 and y >= 1:
        result = x / y
        return result
    else:
        print("Sorry, you can't divide a number by 0. Please try something else.")

num1 = 10
num2 = 0

print(divide_numbers(num1, num2))