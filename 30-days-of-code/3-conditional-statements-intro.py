# Objective
# In this challenge, we learn about conditional statements. Check out the Tutorial tab for learning materials and an instructional video.
# Task
# Given an integer, , perform the following conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Complete the stub code provided in your editor to print whether or not  is weird.
# Input Format
# A single line containing a positive integer, n.
# Constraints
# 1 <= n <=100
# Output Format
# Print Weird if the number is weird; otherwise, print Not Weird.
# Sample Input 0
# 3
# Sample Input 1
# 24

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())

    if not N%2 == 0:
        print('Weird')
    else:        
        if N >= 2 and N <= 5:
            print('Not Weird')

        if N >= 6 and N <= 20:
            print('Weird')

        if N > 20:
            print('Not Weird')

