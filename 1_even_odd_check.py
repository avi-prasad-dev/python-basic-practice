'''
Python Challenge #1 — Even or Odd Checker
Goal

Write a Python program that:

Takes an integer input from the user.
Checks whether the number is even or odd.
Prints the result clearly.

This challenge practices:

User input
Variables
Data types
Conditional statements

Inputs / Outputs
Input

A single integer entered by the user.

Output

Print either:

"Even"
or
"Odd"

Constraints
Assume the user enters a valid integer.
Do not use advanced libraries.
Use if-else.

Example Logic
If number is divisible by 2 → Even
Otherwise → Odd

'''

user_input = int(input("Enter any no. "))

if user_input % 2 == 0:
    print("Even")
else:
    print("Odd")