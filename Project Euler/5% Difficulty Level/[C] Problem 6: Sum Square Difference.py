'''
PROBLEM STATUS: CLOSED

PROBLEM DIFFICULTY LEVEL: 5%

PROBLEM STATEMENT
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
import numpy as np

def sum_square_difference(count):
    '''
    Description:
        Returns the difference between sum of squares of natural numbers and the square of the sum
    Args:
        count (int): The range (i.e. max value) that we want to compute for
    Returns:
        diff (int): The difference (i.e. value required) but in absolute terms because I'm lazy
    '''

    #Creating a list of natural numbers required
    natural_numbers_array = np.linspace(1,count,count)
    #Creating sum of squares and square of sums list
    sum_of_squares = np.sum([num**2 for num in natural_numbers_array])
    square_of_sums = (np.sum(natural_numbers_array))**2
    #Calculating the difference 
    diff = np.abs(sum_of_squares - square_of_sums)
    return(diff)

print(sum_square_difference(100))