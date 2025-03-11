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
    #Creating a list digits to use to create pandigitals
    list_of_digits = [0,1,2,3,4,5,6,7,8,9]
    #Creating the list of pandigitals using permutations but only including the value if the starting digit is not 0
    pandigital_list = [dig for dig in itertools.permutations(list_of_digits,10) if dig[0]!=0]
    #Combining the digits from the itertools (that come as a comma seperated list) into one value and resaving it to my pandigital list
    pandigital_list = list(int(''.join(str(digit) for digit in value)) for value in pandigital_list)
    
    #Creating a list that will store the values that pass the checker test
    pandigital_divisibility_list = []
    #Looping through all existing pandigital lists to check each one's divisibility and appending to our list if true
    for number in pandigital_list:
        if divisibility_checker(number) == True:
            pandigital_divisibility_list.append(number)

    #Printing the final answer, which is the sum of values in this list
    print(np.sum(np.array(pandigital_divisibility_list)))

#Defining a function to evaluate whether a given 10-digit number is 0 to 9 pandigital
def divisibility_checker(value):
    '''
    Description:
        Computes whether a given number satisfies 
    Args:
        value (int): the upperbound of our potential multiples of 3 or 5
    Returns:
        None. Prints the answer.
    '''
    #Defining an array of integers we use for checking divisibility allowing for easy looping
    divisibility_integers = np.array([2,3,5,7,11,13,17])
    #looping through our digits
    for looper in range(len(divisibility_integers)):
        #Subsequently looping through the required digits in our number and checking divisiblity against required integers to return true
        if((int(str(value)[looper+1:looper+4])) % divisibility_integers[looper]) == 0:
            checker = True
        else:
            #Breaking the loop to save computational resource and manpower
            checker = False
            break
    return(checker)

pandigital_generator()