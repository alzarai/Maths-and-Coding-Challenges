'''
PROBLEM STATUS: OPEN

PROBLEM DIFFICULTY LEVEL: 10%

PROBLEM STATEMENT
https://projecteuler.net/problem=69
'''
import numpy as np
import math

def phi(n):
    '''
    Description:
        Computes Eueler's toitient function for a given input integer n. 
    Args:
        n (int): The number we are computing totient for
    Returns:
        phi (int): The nunber of positive integers not exceeding n that are relatively prime to n.
    '''
    #Defining a list of all numbers less than our input. Making sure they are all integers for future consistensy
    nums_less_than_n = np.linspace(1,n,n).astype(int)
    #Only selecting the numbers that are relatively prime (coprime) with n
    relative_coprime_less_than_n = [number for number in nums_less_than_n if ((math.gcd(number,n)) == 1)]
    phi = len(relative_coprime_less_than_n)
    return(phi)

def totient_maximum(S):
    '''
    Description:
        Computes the integer value (n) less than a limit (S) that produces a maximum of the value n_PHI = n/phi(n)
    Args:
        S (int): The upper bound of numbers we are testing for 
    Returns:
        n_maximum (int): The integer value (n) that produces a maximum n_PHI from all relevant n_PHI
    '''
    #Array that will store all values of n/phi(n). The value of n matches the index in looping
    n_PHI_values = []
    for n in range(1,S+1):
        n_PHI = n/phi(n)
        n_PHI_values.append(n_PHI)
    
    #Converting to np array for easier manipulation
    n_PHI_values = np.array(n_PHI_values)
    #The required value will be the value of the argmax of the array + 1
    n_maximum  = n_PHI_values.argmax()+1
    print(n_maximum)

totient_maximum(int(1e6))