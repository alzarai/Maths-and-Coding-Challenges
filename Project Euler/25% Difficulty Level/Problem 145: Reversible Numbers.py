'''
PROBLEM STATUS: COMPLETE

PROBLEM DIFFICULTY LEVEL: 25%

PROBLEM STATEMENT
https://projecteuler.net/problem=145

To solve this, we will create 2 functions namely;
        (1) To reverse a given number
        (2) To check which of the numbers in (1) satisfy the stipulated condition

'''
import numpy as np
#Lets start with all reversible numbers under 20

#Creating a function that has created a list of all numbers (2 digits or greater) below our max_range, and then removes all values with trailing zeroes
def valid_integers(max_range):
    '''
    Description:
        Returns a list of all positive integers n, below a certain maximum, that do not have leading zeroes
    Args:
        max_range (int): The upperbound / limit that we want to compute reversible numbers for
    Returns:
        number_list (ndarray): (m,) The required list of m
    '''
    start_value=11
    #Creates a list of all numbers under our max_range
    total_number_list = np.arange(start_value,max_range+1)
    #Removing all the values with leading zeroes
    number_list = np.array([number for number in total_number_list if number%10 != 0])

def unique_reversing(original_list):
    '''
    Description:
        Returns a list of tuples that contains a value and its reversed form
    Args:
        original_list (ndarray): (m,) A list that containts all the values that need to be reversed
    Returns:
        pairs_list (ndarray): (m/2,m/2) The required list of original numbers and their reversed counterparty
    '''
    #A list that will store the first occurance of any number
    first_occurance = []
    #A list that will store the reversed value of the related number in the first occurance list (numbers will be checked against this list before being added to first occurance list) 
    second_occurance = []
    #List that will store the (number,reversed_number) pair for all possible pairings
    pairs_list = []
    #Loop to reverse through all our numbers, check if it is already an existing pair, and adding to the appropriate lists
    for original_number in original_list:
        #Converting int to string for easier reversal
        num_as_str = list(str(original_number))
        #Reversing our number
        num_as_str_reversed = num_as_str[::-1]
        #Defining the new reversed number as an integer
        reversed_number = int(''.join(str(num) for num in num_as_str_reversed)) 
        #Making sure that only unique pairings are represented in the pairs list - values will only be added if the newly reversed number does has not already been used as an original number
        if(reversed_number not in first_occurance):
            first_occurance.append(original_number)
            second_occurance.append(reversed_number)
    #Creating the list that will store the unique pairing of a number and its reversal
    pairs_list = [(x, y) for x, y in zip(first_occurance, second_occurance)]
    return(pairs_list)


lst = [18,25,52,67,31,13,44,520,205]
print(lst)
print(unique_reversing(lst))


def reversible_number_check(pair_list):
    '''
    Description:
        Returns a list of all pairs that satisfy the reversibility condition (all digits being 0)
    Args:
        pairs_array (ndarray): (m,2) A list that containts all pairs (original and reversed) of potential reversible numbers
    Returns:
        reversible_numbers_array (ndarray): (m) The required list of all unique reversible numbers
    '''