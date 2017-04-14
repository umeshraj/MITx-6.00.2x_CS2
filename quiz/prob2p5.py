#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 11:34:04 2017

@author: umesh
"""

import random

def F():
    mylist = []
    r = 1

    if random.random() > 0.001:
        r = random.randint(1, 10)
        print(r)
    for i in range(r):
        random.seed(0)
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            if number not in mylist:
                mylist.append(number)
    print(mylist)

def G():
    random.seed(0)
    mylist = []
    r = 1

    if random.random() > 0.001:
        r = random.randint(1, 10)
    for i in range(r):
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            mylist.append(number)
            print(mylist)

G()