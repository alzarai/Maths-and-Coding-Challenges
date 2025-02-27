'''
PROBLEM STATUS: SOLVED!

PROBLEM DIFFICULTY LEVEL: 5%

PROBLEM STATEMENT
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000
'''
#Importing out standard libraries - even though we can do without (this problem can very easily be solved without them), I want to get into the habit of actions that are required for bigger problems
import numpy as np
#We'll define a function for good practice
def compute_sum_multiples(value):
    '''
    Description:
        Returns the sum of all multiples of 3 or 5 lower than a given number input.
    Args:
        value (int): the upperbound of our potential multiples of 3 or 5
    Returns:
        None. Prints the answer.
    '''
    #Defining an array of our factors
    factor_array = np.array([3,5])
    
    #Defining a list that will store all the found factors below our threshold
    multiples_list = []

    #Creating the loop that will iterate to give me my desired outcome
    for i in range(value):
        #Since the loop iterator i and the value we are currently checking are the same in value but different uses, we will distinguish between the code easier to read
        potential_multiple = i
        #Testing the modulo of our current value against our factors
        if ((potential_multiple%factor_array[0]==0) or (potential_multiple%factor_array[1]==0)):
            #The current potential multiple is proven to be a multiple hence we can add it to our multiples list
            multiples_list.append(potential_multiple)

    #Once the list is complete, we will convert to a numpy array and calculate our sum
    multiples_array = np.array(multiples_list)
    #Printing our answer
    print(np.sum(multiples_array))

#Running the function
compute_sum_multiples(1000)
 