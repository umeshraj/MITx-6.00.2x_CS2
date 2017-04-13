#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 20:58:12 2017

@author: umesh
"""
import random
def getThree():
    choices = ['R', 'R', 'R', 'B', 'B', 'B']
    tmp = []
    for idx in range(3):
        rand_idx = random.randrange(0, len(choices))
        tmp.append(choices.pop(rand_idx))
    match = tmp == ['R']*3 or tmp == ['B']*3
    return match

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    # Your code here
    num_match = 0
    for iSim in range(numTrials):
        num_match += getThree()
    return num_match/numTrials

print(noReplacementSimulation(5000))