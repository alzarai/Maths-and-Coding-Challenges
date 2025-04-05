'''
PROBLEM STATUS: INCOMPLETE

PROBLEM DIFFICULTY LEVEL: 25%

PROBLEM STATEMENT
https://projecteuler.net/problem=25

'''
import math

def fibo_generator(target_number_of_digits):
    '''
    Description:
        Continiously generates Fibonacci numbers until the first occurance a Fibonacci with the required number of digits
    Args:
        number_of_digits (int): The value of digits we want our searched Fibonacci number to have. Useful to evaluate test and train cases
    Returns:
        index (int): The index of the first term to contain the desired number of digits
    '''
    #Defining the start of the Fibonacci Sequence
    fibo_list = [1,1]
    #Defining the values that will drive the 
    looper_index = 0
    while (True):
        #Defining the next term of the sequence and appending to our list
        new_fibo = fibo_list[looper_index] + fibo_list[looper_index+1]
        fibo_list.append(new_fibo)
        #Checking the number of digits of the current fibonacci number
        digit_count = math.floor(math.log10(new_fibo)) + 1
        #Checking to see if the digit count satisfies our target
        if (digit_count == target_number_of_digits):
            index = fibo_list.index(new_fibo)
            break
        else:
            looper_index+=1
    return(index+1)


print(fibo_generator(1000)) #