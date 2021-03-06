#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 09:41:44 2017

Code for Introduction to Computational Thinking and Data Science
URL: https://goo.gl/B7lYAU
Greedy implementation of knapsack problem
@author: umesh
"""


class Food:
    def __init__(self, name, value, calories):
        self.name = name
        self.value = value
        self.calories = calories

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue()/self.getCost()

    def __str__(self):
        name = self.name
        value = self.getValue()
        cost = self.getCost()
        out = "{0}: <{1}, {2}>".format(name, value, cost)
        return out


def buildMenu(name_list, value_list, calorie_list):
    """ build a list of Food items"""
    menu = []
    for name, value, calorie in zip(name_list, value_list, calorie_list):
        tmp_food = Food(name, value, calorie)
        menu.append(tmp_food)
    return menu


def greedy(items_list, max_cost, key_function):
    """ Implement a greedy algorithm that picks the most valued item first"""
    tmp_list = sorted(items_list, key=key_function, reverse=True)
    cur_cost = 0
    cur_value = 0
    result = []

    for item in tmp_list:
        if cur_cost + item.getCost() <= max_cost:
            result.append(item)
            cur_cost += item.getCost()
            cur_value += item.getValue()
    return result, cur_value


def testGreedy(items, constraint, key_function):
    """ testing greedy"""
    taken, val = greedy(items, constraint, key_function)
    print("Total value: {0}".format(val))
    for item in taken:
        print(' ', item)


def testGreedy_many(foods, max_units):
    print("Using greedy by value to allocate {0} calories".format(max_units))
    testGreedy(foods, max_units, Food.getValue)

    print("Using greedy by cost to allocate {0} calories".format(max_units))
    testGreedy(foods, max_units, lambda x: 1/Food.getCost(x))

    print("Using greedy by density to allocate {0} calories".format(max_units))
    testGreedy(foods, max_units, Food.density)


def maxVal(item_list, rem_space):
    """ search tree to find best combination of items in knapsack
    Returns:
        (value, items_chosen)
    """
    if item_list == [] or rem_space == 0:  # no items or space
        result = (0, ())
    else:
        next_item = item_list[0]
        if next_item.getCost() > rem_space:
            result = maxVal(item_list[1:], rem_space)
        else:
            with_val, with_list = maxVal(item_list[1:],
                                              rem_space-next_item.getCost())
            with_val += next_item.getValue()

            without_val, without_list = maxVal(item_list[1:],
                                                    rem_space)
            if with_val > without_val:
                result = (with_val, with_list + (next_item, ))
            else:
                result = (without_val, without_list)
    return result


def testMaxVal(foods, maxUnits, printItems = True):
    print('Use search tree to allocate', maxUnits,
          'calories')
    val, taken = maxVal(foods, maxUnits)
    print('Total value of items taken =', val)
    if printItems:
        for item in taken:
            print('   ', item)


if __name__ == "__main__":
    names = ['wine', 'beer', 'pizza', 'burger', 'fries',
             'cola', 'apple', 'donut', 'cake']
    values = [89, 90, 95, 100, 90, 79, 50, 10]
    calories = [123, 154, 258, 354, 365, 150, 95, 195]
    foods = buildMenu(names, values, calories)
    testGreedy_many(foods, 1000)

    # implement a flexible greedy algorithm
    testMaxVal(foods, 750)
