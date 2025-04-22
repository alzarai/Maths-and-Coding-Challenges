'''
PROBLEM STATUS: OPEN

PROBLEM DIFFICULTY LEVEL: 15%

PROBLEM STATEMENT
https://projecteuler.net/problem=205
'''
import itertools
import numpy as np

'''
Lets start this problem simpler. Let us define user1 with 2 dice that can choose values [2,5] and user2 with 2 dice of values [3,4]
We know that user1 values = [(2,2),(2,5),(5,2),(5,5)] and user2 values = [(3,3,(3,4),(4,3),(4,4)]
'''
user_1=(5,7)
user_2=(1,2)
u1 = list(itertools.product(user_1, repeat=len(user_1)))
u1_sum = list(map(lambda x: sum(x),u1))
u2 = list(itertools.product(user_2, repeat=len(user_2)))
u2_sum = list(map(lambda x: sum(x),u2))
print(u1_sum,u2_sum)

totals = (len(u1_sum) + len(u2_sum))
u1_greater = 0
for u1_val in u1_sum:
    for u2_val in u2_sum:
        if u1_val > u2_val:
            u1_greater+=1

print(u1_greater/totals)
