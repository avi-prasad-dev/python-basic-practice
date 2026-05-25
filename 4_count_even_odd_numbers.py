'''
Python Challenge #4 — Count Even and Odd Numbers in a List
Goal

Write a program that:

Creates a list of numbers
Counts:
how many even numbers exist
how many odd numbers exist
Prints both counts

'''
number_list = [12, 7, 9, 14, 20, 33, 41, 50]
# even_count = [] this takes more memory 
# odd_count = []

even_count = 0 
odd_count = 0
for numbers in number_list:
    if numbers % 2 == 0:
        # even_count.append(numbers) -> instead of this do following
        even_count += 1
    else:
        # odd_count.append(numbers)
        odd_count +=1

print(f"Even count: {even_count}")
print(f"Odd count {odd_count}")