#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 14:15:10 2017

@author: umesh
"""

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for
        the largest value in L then for the second largest, and so on to
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does
                not yield a set of multipliers such that the equation sums to 's'
    """
    N = len(L)
    m = []
    s_right = 0
    for l in L:
        m_new = (s-s_right)//l
        s_right += l*m_new
        m.append(m_new)

    print("M: {0}".format(m))
    if s_right == s:
        return  sum(m)
    else:
        return 'no solution'


print(greedySum([2, 1], 3))