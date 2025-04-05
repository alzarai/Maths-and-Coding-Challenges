'''
PROBLEM STATUS: OPEN (need to find way to reduce run time?? At the moment its too computationally intense for your laptop - checking for 1e6 doesn't finish)

PROBLEM DIFFICULTY LEVEL: 20%

PROBLEM STATEMENT
https://projecteuler.net/problem=145

To solve this, we will create 2 functions namely;
        (1) To create a list of all possible numbers (no leading 0s) along with their reversed forms, such that each number only occurs once
        (2) To check which of the numbers in (1) satisfy the stipulated condition, and how many such numbers (number and its pair) exist

'''
import numpy as np

#Creating a function that creates the pair of uniquely reversed numbers
def unique_reversed_pair_generator(max_range):
    '''
    Description:
        Returns a list of tuples that contains a value and its reversed form, after creating a list of all positive integers n, below a certain maximum, that do not have leading zeroes
    Args:
        max_range (int): The upperbound / limit that we want to compute reversible numbers for
    Returns:
        pairs_list (ndarray): (m/2,m/2) The required list of original numbers and their reversed counterparty
    '''
    start_value=11
    #Creates a list of all numbers under our max_range
    total_number_list = np.arange(start_value,max_range+1)
    #Removing all the values with leading zeroes
    number_list = np.array([number for number in total_number_list if number%10 != 0])

    #A list that will store the first occurance of any number
    first_occurance = []
    #A list that will store the reversed value of the related number in the first occurance list (numbers will be checked against this list before being added to first occurance list) 
    second_occurance = []
    #List that will store the (number,reversed_number) pair for all possible pairings
    pairs_list = []
    #Loop to reverse through all our numbers, check if it is already an existing pair, and adding to the appropriate lists
    for original_number in number_list:
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
    pairs_list = np.array([(x, y) for x, y in zip(first_occurance, second_occurance)])
    #Executing the next function that will check for reversible numbers within our pairs list
    number_of_reversible_numbers = len(reversible_number_check(pairs_list))*2
    return(number_of_reversible_numbers)


def reversible_number_check(pair_list):
    '''
    Description:
        Returns a list of all pairs that satisfy the reversibility condition (all digits being odd)
    Args:
        pair_list (ndarray): (n,n) A list that containts all pairs (original and reversed) of potential reversible numbers
    Returns:
        reversible_numbers_array (ndarray): (p) The required list of all unique reversible numbers. Array size reduced from n to p
    '''
    #A list that will store boolean values on whether a giving pairing's sum satisifies the checked condiiton or not
    truth_list  = []
    #Looping through all our current examples
    for pair in pair_list:
        #Calculating the property to be checked, namely sum[n + reverse(n)]
        pair_sum = np.sum(pair)
        #Converting to a (string) list to check across all digits
        pair_sum_str = list(str(pair_sum))
        #Looping through all digits of the current pair sum
        for x in range(len(pair_sum_str)):
            #Checking to see if the current digit is an odd number 
            if ((int(pair_sum_str[x])%2) != 0):
                odd_check = True
            else:
                odd_check = False
                break
        truth_list.append(odd_check)
    #Converting the boolean list to a numpy array for easier manipulation, now that all additions to the list have been completed
    truth_list = np.array(truth_list)
    #Creating our required list of only the pairings that satisified the condition (returned "True" in the truth list / odd checker)
    reversible_pairs_array = pair_list[truth_list]
    return(reversible_pairs_array)

#Evaluating the functions and printing the answer given to us
print(unique_reversed_pair_generator(int(1e5))) #As the problem mentions, the solution is 120 reversible numbers below 1,000 (1e4)