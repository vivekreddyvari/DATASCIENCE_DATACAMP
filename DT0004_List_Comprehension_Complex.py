# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 16:55:59 2019

@author: M63A520
"""

# complicated list comprehension 
# with conditions

list_compre = [num ** 2 for num in range(10) if num % 2 ==0 ]
print(list_compre) #output [0, 4, 16, 36, 64]

list_compre_1 = [num ** 2 if num % 2 == 0 else 0 for num in range(10)]
# output is the even number that is squared and zeros are the odd number that are squared

print(list_compre_1) # output([0, 0, 4, 0, 16, 0, 36, 0, 64, 0])

# dictionary comprehensions with new dictionaries
 # 1.  use curly braces {} instead of []

# Positive & Negative numbers
pos_neg = {num: -num for num in range(9)}
print(pos_neg)

# Sum of n numbers ((n*(n+1)/2))
sum_of_n_numbers = {n: (n * (n + 1) / 2) for n in range(1, 21)}
print(sum_of_n_numbers)


# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) > 6 ]

# Print the new list
print(new_fellowship)

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member if len(member) >= 7 else " " for member in fellowship]

# Print the new list
print(new_fellowship)

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = {member: len(member) for member in fellowship }

# Print the new list
print(new_fellowship)

