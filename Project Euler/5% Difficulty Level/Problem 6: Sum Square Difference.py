'''
PROBLEM STATUS: COMPLETE

PROBLEM DIFFICULTY LEVEL: 5%

PROBLEM STATEMENT
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
import numpy as np

def sum_square_difference(count):
    #Creating a list of natural numbers required
    natural_numbers_array = np.linspace(1,count,count)
    sum_of_squares = np.sum([num**2 for num in natural_numbers_array])
    square_of_sums = (np.sum(natural_numbers_array))**2
    diff = sum_of_squares - square_of_sums
    return(np.abs(diff))

print(sum_square_difference(100))