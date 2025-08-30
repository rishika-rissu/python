#Task 1: check if a number is even or odd 

#1. Takes an integer input from the user.

"""user_input = int(input("Enter an integer: "))
print("You entered:", user_input)"""

#checks whether the number is ever or odd using an if-else statement. 

"""num = int(input("Enter an integer:"))
if num % 2 == 0:
    print("the number is even.")
else:
    print("the number is odd.")
"""
    # Displays the result accordingly.
    #Enter a number: 7
    #7 is an odd number.

    #Enter a number: 12
    #12 is an even number.
"""
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("is an even number.")
else:
    print("is an odd number.")
"""

    #Task 2: sum of intrgers from 1 to 50 using a loop

    # Uses a for loop to iterate over number from 1 to 50.

'''for i in range(1,51):
  print(i)'''

  # Calculates the sum of all integers in this range.

 

total_sum = 1
for i in range(1, 51):
    total_sum += i
print("Sum of integers from 1 to 50 is:", total_sum)

#  Displays the final sum.

#the sum of numbers from 1 to 50 is:1275
 
total_sum = 0
for i in range(1, 51):
    total_sum += i
print("Sum of integers from 1 to 50 is:", total_sum)