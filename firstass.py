#Task1
#Takes two numbers as input from the user

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#  Performs the basic mathematical operations on these two numbers:(+, -, *, \)

num1 = 8
num2 = 9
# performing basic mathematical operations


print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)

# display the results of each operation performed, for example:  Expected output: the output should include the result of each operation performed, for example:
#Enter the first number : 5
#Enter the second number : 10

# Addition : 15
#Subtraction : -5
#Multiplication : 50
#Division : 0.5

num1 = 5 
num2 = 10 

addition = num1 + num2
subtraction  = num1 - num2
multiplication = num1 * num2
division = num1 / num2

#Displaying the results 
print("addition:", addition)
print("subtraction:", subtraction)
print("multiplication:", multiplication)
print("division:", division)


    #Task 2: create a personalized greeting 
    # Takes a user's first name and last name as input. 

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print("First Name:", first_name)
print("Last Name:", last_name)

#Concatenates the first name and last name into a full name.

first_name = input("Enter your first name: ")

last_name = input("Enter your last name: ")

full_name = first_name + last_name 

print("full_name:", full_name)

# prints a personalized greeting massage using the full name.
#Expected output:
#The program should output a greeting like:

#Enter your first name:John
#Enter your last name: Doe

#Hello, John Doe! welcome to the python program.

first_name = input("Enter your first name: ")

last_name = input("Enter your last name: ")

full_name = first_name + " " + last_name
e
print(f"Hello, {full_name}! Welcome to the Python program.")