'''
Python Challenge #2 — Sum of Numbers from 1 to N

Goal

Write a program that:

    Takes an integer N from the user Calculates the sum from 1 to N Prints the final sum

This challenge practices:

    Loops
    Variables
    Input/output
    Arithmetic operations

Constraints
    N will be a positive integer Use a for loop Do NOT use Python’s built-in sum() function

'''

user = int(input("Enter a number. "))
total_sum = 0
for number in range(1, user+1):
    total_sum = total_sum + number


print(total_sum)



