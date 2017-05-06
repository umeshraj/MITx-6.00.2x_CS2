#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 10:24:36 2017

@author: umesh
"""

import random
def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here
    num_succ = 0
    for idx in range(numTrials):
        tmp = random.sample(population=[1, 1, 1, 1, 0, 0, 0, 0], k=3)
        if (sum(tmp) == 0) or (sum(tmp) == 3):
            num_succ += 1
    return num_succ/numTrials

if __name__ == "__main__":
    frac = drawing_without_replacement_sim(10000)
    print("Fraction of succ: {0}".format(frac))