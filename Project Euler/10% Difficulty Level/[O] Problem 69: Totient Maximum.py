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
    relative_coprime_less_than_n = nums_less_than_n[np.gcd(nums_less_than_n,n) == 1]
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
    #Defining array of all the numbers we need to screen
    n_values = np.arange(1,S+1)
    #Vecrtorising our phi function so that it better forms for numpy arrays
    phi_n_vec = np.vectorize(phi)

    #Generating a new array that computes the required value n_PHI = n/phi(n)
    n_PHI_values = n_values/phi_n_vec(n_values)
    
    #The required value will be the value of the argmax of the array + 1
    n_maximum  = n_PHI_values.argmax()+1
    print(n_maximum)

#totient_maximum(int(1e6))
import numpy as np

def compute_totients(N):
    totients = np.arange(N + 1)
    for p in range(2, N + 1):
        if totients[p] == p:  # This means p is prime
            totients[p::p] -= totients[p::p] // p
    return totients

S = int(1e6)
totients = compute_totients(S)
origi = np.arange(2,S+1)
ans = origi/totients[2:]

argmax = np.argmax(ans)


#print(origi)
#print((totients[2:]))
print(argmax+2)