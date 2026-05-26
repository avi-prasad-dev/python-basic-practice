'''
Python Challenge #5 — Find the Largest Number in a List
Goal

Write a program that finds the largest number in a list manually.

'''
number_list = [45, 12, 89, 23, 67, 100, 34]

largest_number = number_list[0]

for numbers in number_list:
    if numbers > largest_number:
        largest_number = numbers

print(f"Largest number: {largest_number}")