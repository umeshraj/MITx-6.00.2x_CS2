#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 19:59:19 2017

@author: umesh
"""

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    #YOUR CODE HERE
    N = len(L)
    max_sum = L[0]
    for left_idx in range(N):
        for right_idx in range(N):
            cur_sum = sum(L[left_idx:right_idx+1])
            if cur_sum > max_sum:
                max_sum = cur_sum
    return max_sum

L = [3, 4, -1, 5, -4]
#L = [3, 4, -8, 15, -1, 2]
print(max_contig_sum(L))