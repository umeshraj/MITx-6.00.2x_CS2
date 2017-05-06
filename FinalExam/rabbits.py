import random
import pylab

# Global Variables
#MAXRABBITPOP = 1000
#CURRENTRABBITPOP = 500
#CURRENTFOXPOP = 30

#MAXRABBITPOP = 1000
#CURRENTRABBITPOP = 1000
#CURRENTFOXPOP = 30

#CURRENTRABBITPOP = 1000
#MAXRABBITPOP = 1000
#CURRENTFOXPOP = 50

# Calling foxGrowth with CURRENTRABBITPOP = 1,
# MAXRABBITPOP = 1000, CURRENTFOXPOP = 1 should not increase the population.
#CURRENTRABBITPOP = 1
#MAXRABBITPOP = 1000
#CURRENTFOXPOP = 1

# Test the simulation with CURRENTRABBITPOP = 10, CURRENTFOXPOP = 20, MAXRABBITPOP = 100
CURRENTRABBITPOP = 10
CURRENTFOXPOP = 20
MAXRABBITPOP = 100

# Test the simulation with CURRENTRABBITPOP = 10, CURRENTFOXPOP = 20, MAXRABBITPOP = 100

CURRENTRABBITPOP = 10
CURRENTFOXPOP = 20
MAXRABBITPOP = 100



def rabbitGrowth():
    """
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up,
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # TO DO
    prob_new_rabbit = 1 - CURRENTRABBITPOP/MAXRABBITPOP
    num_new_rabbits = 0
    for i_rabbit in range(CURRENTRABBITPOP):
        if random.random() < prob_new_rabbit:
            num_new_rabbits += 1
    CURRENTRABBITPOP += num_new_rabbits
    CURRENTRABBITPOP = min(CURRENTRABBITPOP, MAXRABBITPOP)
    #print(CURRENTRABBITPOP)


def foxGrowth():
    """
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    # decide if fox is going to eat a rabbit
    num_new_foxes = 0
    for i_fox in range(CURRENTFOXPOP):
        if CURRENTRABBITPOP <= 10:  # cannot eat rabbit
            eat_rabbit = False
        else:  # it can eat a rabbit
            eat_rabbit = random.random() < CURRENTRABBITPOP/MAXRABBITPOP

        # change populations based on whether a rabbit was eaten or not
        if eat_rabbit:  # reduce rabbit pop and increase fox pop
            CURRENTRABBITPOP -= 1
            if random.random() < 1/3:
                num_new_foxes += 1
        else:  # did not eat rabbit
            # fox dies w/ p=0.1
            if random.random() < 0.1 and CURRENTFOXPOP > 10:
                num_new_foxes -= 1
    CURRENTFOXPOP += num_new_foxes
    #print(CURRENTFOXPOP)


def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    rabbit_populations = []
    fox_populations = []
    for iStep in range(numSteps):
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
        rabbitGrowth()
        foxGrowth()
    return (rabbit_populations, fox_populations)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    rab, fox = runSimulation(200)
    plt.plot(rab, label='Rabbit')
    plt.plot(fox, label='Fox')
    plt.hlines(10, 0, 200)
    plt.legend()
#    rabbitGrowth()
#    rabbitGrowth()
#    foxGrowth()
#    foxGrowth()
#    for i in range(20):
#        foxGrowth()
