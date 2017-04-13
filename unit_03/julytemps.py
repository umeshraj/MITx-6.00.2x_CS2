#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 21:42:04 2017

@author: umesh
"""

def loadFile():
    inFile = open('julytemps.txt')
    high = []
    low = []
    for line in inFile:
        fields = line.split()
        # FILL THIS IN
        if len(fields) != 3 or 'Boston' == fields[0] or 'Day' == fields[0]:
            continue
        else:
            high.append(int(fields[1]))
            low.append(int(fields[2]))
    return (low, high)

loadFile()