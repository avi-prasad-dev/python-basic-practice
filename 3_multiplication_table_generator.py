'''
Python Challenge #3 — Multiplication Table Generator
Goal

Write a program that:

Takes a number from the user
Prints its multiplication table from 1 to 10
'''

num_for_multiplication = int(input("Enter a number: "))

for table in range(1, 11):
    print(f"{num_for_multiplication} x {table} = {num_for_multiplication * table}")