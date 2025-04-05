'''
PROBLEM STATUS: CLOSED

PROBLEM DIFFICULTY LEVEL: 5%

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
        index+1 (int): The index of the first term to contain the desired number of digits
    '''
    #Defining our list with the start of the Fibonacci Sequence and the value that will be used to index the list
    fibo_list = [1,1] 
    looper_index = 0
    while (True):
        #Defining the next term of the sequence and appending to our list
        new_fibo = fibo_list[looper_index] + fibo_list[looper_index+1]
        fibo_list.append(new_fibo)
        #Checking the number of digits of the current fibonacci number
        digit_count = math.floor(math.log10(new_fibo)) + 1
        #Checking to see if the digit count satisfies our target
        if (digit_count == target_number_of_digits):
            #if satisfied, the required indext is the index of this value
            index = fibo_list.index(new_fibo)
            break
        else:
            looper_index+=1
    #Returning the (positive number value) index of our required value
    return(index+1)

#Evaluating our function to generate our answer. Argument is the number of digits we're looking for
print(fibo_generator(1000)) #As the problem mentions, the solution is 12th term for the first term to contain 3 digits