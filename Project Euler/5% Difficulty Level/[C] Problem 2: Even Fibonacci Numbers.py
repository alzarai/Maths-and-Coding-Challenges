'''
PROBLEM STATUS: CLOSED

PROBLEM DIFFICULTY LEVEL: 5%

PROBLEM STATEMENT
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''
import numpy as np

def even_fibos():
    '''
    Description:
        Returns the sum of all even-valued Fibonacci numbers under four million
    Args:
        None
    Returns:
        even_fibo_sum (unt): The sum of the list that contained all even Fibonacci numbers under four million
    '''
    #Defining the start of the Fibonacci Sequence
    fibo_list = [1,1]
    looper = 0
    while (fibo_list[-1] < 4e6):
        #Defining the next term of the sequence and appending to our list
        fibo_list.append(fibo_list[looper] + fibo_list[looper+1])
        looper+=1
    #Using list comprehension to filter only the even Fibonacci numbers
    even_fibo_list = [num for num in fibo_list if (num%2)==0]
    #Converting to a numpy array for easy summing
    even_fibo_sum = np.sum(np.array(even_fibo_list))
    return(even_fibo_sum)
print(even_fibos())