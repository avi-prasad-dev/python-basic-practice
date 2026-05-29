'''
Python Challenge #6 — Count Frequency of Characters
Goal

Write a program that counts how many times each character appears in a string.

'''

words = input("Enter a word: ")
character_count = {}

for word in words:
    if word in character_count:
        character_count[word]+=1
    else:
        character_count[word]=1

print(character_count)



