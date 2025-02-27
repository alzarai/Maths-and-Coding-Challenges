'''
PROBLEM STATUS: In Progress

PROBLEM DIFFICULTY LEVEL: 70%

PROBLEM STATEMENT
https://projecteuler.net/problem=282
'''

#Importing out standard libraries
import numpy as np
#We'll define a function for good practice
def ackerman_function(m,n):
    '''
    Description:
        Defines the Ackerman function and evaluates its value given two inputs m and n
    Args:
        m (int) and n (int): the arguments to the Ackerman function
    Returns:
        The value of the evaluated Ackerman function
    '''
    #It is clear that this function will continue to run itself until we reach a case where m has been reduced to 0
    #Defining the variable that holds the value of Ackerman function and initialising to 0
    
    function_evaluation = 0
    #Based on the definition, the Ackerman function is a piece wise function. Our first task is to define which case/branch of the function we are dealing with
    if(m==0):
        function_evaluation = n+1
        return(function_evaluation)
    elif((m>n) and (n==0)):
        #Recalling the ackerman function
        return(ackerman_function(m-1,1))
    else:
        #Recalling the ackerman function
        return(ackerman_function(m-1,ackerman_function(m,n-1)))

print(ackerman_function(3,3))

'''#Defining function for the summation of Ackerman from 0 to sum_range
def sum_ackerman(sum_range):
    for i in range(sum_range):'''

