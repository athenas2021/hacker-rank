#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    string = str(input())
    list = list()
    for i in range(len(string)):
        list = string.split(" ")
    
    list.reverse()
    spaced_string = ''
    for y in range(len(list)):
        if y == 0:
            spaced_string = list[y]
        else:
            spaced_string += ' '
            spaced_string += list[y]

    print(spaced_string)
