#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 11:04:38 2017

@author: umesh
"""

import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    # TODO
    pylab.hist(values, bins=numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title:
        pylab.title(title)
    pylab.show()


# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    # TODO
    run_list = []
    for iTrial in range(numTrials):
        roll = rollDie(die, numRolls)
        run_list.append(getLongestRun(roll))

    makeHistogram(run_list, numBins=10, xLabel='Runs', yLabel='Counts',
                  title='Rolling die')
    mean_std = getMeanAndStd(run_list)
    return round(mean_std[0], 3)


def rollDie(die, numRolls):
    rolls = []
    for iRoll in range(numRolls):
        rolls.append(die.roll())
    return rolls

def getLongestRun(in_list):
    """compute the longest run in the input list"""
    max_run = 1
    cur_run = 1
    for idx in range(1, len(in_list)):
        if in_list[idx] == in_list[idx-1]:
            cur_run += 1
        else:
            if cur_run > max_run:
                max_run = cur_run
            cur_run = 1  # reset cur_run
    # update the cur_run in case last run is at end of list
    if cur_run > max_run:
        max_run = cur_run
    return max_run

# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))

assert(getLongestRun([1, 4, 3]) == 1)
assert(getLongestRun([1, 3, 3, 2]) == 2)
assert(getLongestRun([5, 4, 4, 4, 5, 5, 2, 5]) == 3)
