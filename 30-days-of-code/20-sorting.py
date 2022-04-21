#!/bin/python3

import math
import os
import random
import re
import sys


    

def bubblesort(array):
    def swap(x,y):
        valor1 = array[x]
        valor2 = array[y]
        array[x] = valor2
        array[y] = valor1

    #print(a)
    arrayx = array
    numberOfSwaps = 0
    for i in range(len(arrayx)):
        
        for j in range(len(arrayx)):
            if len(arrayx) > j+1:
                if arrayx[j] > arrayx[j+1]:
                    swap(j, j+1)
                    numberOfSwaps += 1
        
        if (numberOfSwaps == 0):
            break
    return arrayx, numberOfSwaps

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    
    teste,sw = bubblesort(a)
    print(f'Array is sorted in {sw} swaps.')
    print(f'First Element: {teste[0]}')
    print(f'Last Element: {teste[len(teste)-1]}')
    # Write your code here

    
    
