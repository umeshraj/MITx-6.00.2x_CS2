#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:26:27 2017

@author: umesh
"""

import random
def genEven():
    '''
    Returns a random number x, where 0 <= x < 100
    '''
    # Your code here
    x = random.randint(0, 99)
    x = x//2 * 2
    return x