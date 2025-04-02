'''
PROBLEM STATUS: COMPLETE!

PROBLEM DIFFICULTY LEVEL: 5%

PROBLEM STATEMENT
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''
import numpy as np

def even_fibos():
    fibo_list = [1,2]
    looper = 0
    while (fibo_list[-1] < 4e6):
        fibo_list.append(fibo_list[looper] + fibo_list[looper+1])
        looper+=1
    #Even fibonacci numbers
    even_fibo_list = [num for num in fibo_list if (num%2)==0]
    #Converting to a numpy array for easy summing
    even_fibo_sum = np.sum(np.array(even_fibo_list))
    return(even_fibo_sum)
print(even_fibos())