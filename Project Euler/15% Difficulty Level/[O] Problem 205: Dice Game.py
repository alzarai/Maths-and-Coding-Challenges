'''
PROBLEM STATUS: OPEN

PROBLEM DIFFICULTY LEVEL: 15%

PROBLEM STATEMENT
https://projecteuler.net/problem=205
'''
import itertools


pyramidal_values = [1,2,3,4]
cubic = [1,2,3,4,5,6]

g1 = [1,2,3,4]
g2 = [3,4]

total_vals = list(itertools.combinations((g1),2))
itertools.combinations()
print(total_vals)
