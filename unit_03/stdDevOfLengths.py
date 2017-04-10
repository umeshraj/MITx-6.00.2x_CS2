#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 14:34:05 2017

@author: umesh
"""

import math
def stdDevOfLengths(L):
    if len(L) == 0:
        return float('NaN')
    list_len = []
    for item in L:
        list_len.append(len(item))

    # compute mean and variance
    N = len(list_len)
    my_sum = 0
    for l in list_len:
        my_sum += l
    my_mean = my_sum/N

    my_var = 0
    for l in list_len:
        my_var += (l-my_mean)**2
    my_var = math.sqrt(my_var/N)

    return my_var


L = ['a', 'z', 'p']
print(stdDevOfLengths(L))

L = ['apples', 'oranges', 'kiwis', 'pineapples']
print(stdDevOfLengths(L))
