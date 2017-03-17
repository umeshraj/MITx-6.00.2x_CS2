###########################
# 6.00.2x Problem Set 1: Space Cows

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')

    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    pass


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    pass_list = dict_to_list(cows)
    partitions = get_partitions(pass_list)

    min_num_trips = len(pass_list)
    min_part = None
    for part_list in partitions:
        trip_weights = get_partition_weight(part_list)
        valid_trip = all([x < limit for x in trip_weights])
        if valid_trip and len(trip_weights) < min_num_trips:
            min_num_trips = len(trip_weights)
            min_part = part_list

    pass_list = get_names_mult_trips(min_part)
    return pass_list

# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


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


def dict_to_list(pass_dict):
    pass_list = []
    for k, v in pass_dict.items():
        passenger = Passenger(k, v)
        pass_list.append(passenger)
    return pass_list


def get_weight(pass_list):
    cur_weight = 0
    for item in pass_list:
        cur_weight += item.getWeight()
    return cur_weight


def get_partition_weight(part_list):
    part_weight = []
    for part in part_list:
        part_weight.append(get_weight(part))
    return part_weight

def get_names_one_trip(pass_list):
    name_list = []
    for item in pass_list:
        name_list.append(item.getName())
    return name_list

def get_names_mult_trips(trip_list):
    trip_names = []
    for pass_list in trip_list:
        trip_names.append(get_names_one_trip(pass_list))
    return trip_names

"""
Here is some test data for you to see the results of your algorithms with.
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10

#cows = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
#limit=10

#cows = {'Horns': 25, 'Miss Bella': 25, 'Boo': 20, 'MooMoo': 50,
#        'Lotus': 40, 'Milkshake': 40}
#limit = 100

#cows = {'Daisy': 50, 'Betsy': 65, 'Buttercup': 72}
#limit = 75

print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))
