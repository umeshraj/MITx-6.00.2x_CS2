#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 16:58:37 2017
Problem set1:
@author: umesh
"""

class Passenger:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.transported = False

    def getWeight(self):
        return self.weight

    def getName(self):
        return self.name

    def getTransported(self):
        return self.transported

    def __str__(self):
        out_str = "{0}:{1}".format(self.getName(), self.getWeight())
        return out_str


def greedy(pass_list, max_weight):
    pass_list = sorted(pass_list, key=Passenger.getWeight, reverse=True)
    cur_weight = 0
    transport_names = []
    remaining_list = []
    for item in pass_list:
        if item.getWeight() + cur_weight <= max_weight:
            transport_names.append(item.getName())
            cur_weight += item.getWeight()
        else:
            remaining_list.append(item)
    return transport_names, remaining_list



def dict_to_list(pass_dict, max_limit):
    pass_list = []
    for k, v in pass_dict.items():
        passenger = Passenger(k, v)
        pass_list.append(passenger)
    return pass_list


def greedy_cow_transport(pass_dict, max_limit):
    num_passengers = len(pass_dict)
    pass_list = dict_to_list(pass_dict, max_limit=max_limit)

    num_transported = 0
    transport_list = []
    while num_transported < num_passengers:
        trans_list, remain_list = greedy(pass_list, max_limit)
        transport_list.append(trans_list)
        num_transported += len(trans_list)
        pass_list = remain_list
    return transport_list


if __name__ == "__main__":
    pass_dict = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
    transport_list = greedy_cow_transport(pass_dict, 10)
    print(transport_list)
