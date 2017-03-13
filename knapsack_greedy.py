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

foods = ['apple', 'burger' , 'shake']
values = [10, 50, 100]
calories = [1, 200, 350]
menu = buildMenu(foods, values, calories)
