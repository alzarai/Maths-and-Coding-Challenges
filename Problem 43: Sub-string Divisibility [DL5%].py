'''
PROBLEM STATUS: IN PROGRESS

PROBLEM DIFFICULTY LEVEL: 5%

PROBLEM STATEMENT
https://projecteuler.net/problem=43
'''

'''
To solve this, we will create 2 functions namely;
        (1) To generate a list of all 10-digit pandigital numbers out of all possible 10-digit numbers
        (2) To check which of the numbers in (1) satisfy the stipulated condition

'''
#Importing our favourite library. For the moment, use of the libraries is arbitrary (sometimes will try to develop code that already exists in libraries so I can sharpen my thinking capabilities)
import numpy as np
import itertools

#Defining a function to generate all 10-digit pandigital numbers 
def pandigital_generator():
    '''
    Description:
        Generates a list of all 3,265,920 (10!-9! = 9*9!) possible 10-digit pandigital numbers out of 9,000,000,000 (9*10^9)possible 10-digit numbers. 
    Args:
        None. 
    Returns:
        pandigital_array (ndarray) : Array of size 3,265,920 that contains all existing pandigital numbers
    '''
    #Defining the number of pandigital numbers 
    number_of_pandigitals = 3265920 
    list_of_digits = [0,1,2,3,4,5,6,7,8,9]
    #Creating the list that will store our discovered pandigital and be converteed to array at the end
    pandigital_list = list(itertools.permutations(list_of_digits,10))
    print(pandigital_list)

    


pandigital_generator()

#Defining a function to evaluate whether a given 10-digit number is 0 to 9 pandigital
def pandigital_checker(value):
    '''
    Description:
        Computes whether a given number satisfies 
    Args:
        value (int): the upperbound of our potential multiples of 3 or 5
    Returns:
        None. Prints the answer.
    '''
    #Defining an array of our factors
    factor_array = np.array([3,5])