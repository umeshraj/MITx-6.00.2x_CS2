#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 13:21:53 2017

@author: umesh
"""
import numpy as np


def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    bin_list = gen_binary(len(choices))
    # compute the sum for each combo
    total_list = []
    for binval in bin_list:
        total_list.append(np.dot(choices, binval))

    best_combo = pick_best(total, total_list, bin_list)
    return np.array(best_combo)


def pick_best(goal, total_list, bin_list):
    """pick best combination"""
    best_combo = bin_list[0]
    best_err = np.inf
    best_sum = np.inf
    for binval, total in zip(bin_list, total_list):
        cur_err = goal - total
        if cur_err == 0:  # perfect match
            best_err = 0
            # find the binval with min ones
            if np.sum(binval) < best_sum:
                best_combo = binval
                best_sum = np.sum(binval)
        elif (cur_err > 0) and (cur_err < best_err):  # found better match that before
            best_combo = binval
    return best_combo


def gen_binary(num_choices):
    N = num_choices
    bin_list = []
    for i in range(2**N):
        tmp_binary = bin(i)
        bin_string = tmp_binary[2:]
        extra_zeros = N - len(bin_string)
        bin_string = '0'*extra_zeros + bin_string
        np_array = [int(x) for x in bin_string]
        bin_list.append(np_array)
    return bin_list

if __name__ == "__main__":
    #ur = find_combination([1, 81, 3, 102, 450, 10], 9)
    #ur = find_combination([10, 100, 1000, 3, 8, 12, 38], 1171)
    # print(ur)
    test_dict ={
            1: ([1,2,2,3], 4, np.array([0, 1, 1, 0])),
            2: ([1,1,3,5,3], 5, np.array([0, 0, 0, 1, 0])),
            3: ([1,1,1,9], 4, np.array([1, 1, 1, 0])),
            4: ([3, 10, 2, 1, 5], 12, np.array([0, 1, 1, 0, 0])),
            5: ([105, 10, 9, 6, 4], 120, np.array([1, 0, 1, 1, 0])),
            6: ([10, 100, 1000, 3, 8, 12, 38], 1171, [1, 1, 1, 1, 1, 1, 1])
            }


    for key, val in test_dict.items():
        np.testing.assert_array_equal(find_combination(val[0], val[1]),
                                      val[2])

