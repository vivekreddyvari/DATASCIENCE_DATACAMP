# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 16:34:05 2019

@author: M63A520
"""

# LIst comprehensions

imp_dates = [1985, 1986, 1990, 1992]
imp_dates_family = [num + 1 for num in imp_dates]
print(imp_dates_family) # output: [1986, 1987, 1991, 1993]

results = [num for num in range(11)]
print(results) #output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list comprehensions replaces the nested for loops
pairs_2 = [(num1, num2) for num1 in range(0,2) for num2 in range(6,8)]
print(pairs_2) # output : [(0, 6), (0, 7), (1, 6), (1, 7)]

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(0,5)] for row in range(0,5)]

# Print the matrix
for row in matrix:
    print(row)

#output :
    #[0, 1, 2, 3, 4]
    #[0, 1, 2, 3, 4]
    #[0, 1, 2, 3, 4]
    #[0, 1, 2, 3, 4]
    #[0, 1, 2, 3, 4]

