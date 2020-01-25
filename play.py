from mancala import Board
from brain import Brain
from evolver import Evolver
from math import floor
from random import shuffle, sample, random
import os
import numpy as np
from matplotlib import pyplot as plt


handle = None
def plot(stats_per_iteration):
    if not os.path.exists('./figures'):
        os.mkdir('./figures')

    plt.axis([0, len(stats_per_iteration) + 10, 0, 20])
    plt.ion()
    x = [ s['avg rounds per game'] for s in stats_per_iteration  ]
    x2 = [ s['avg score'] for s in stats_per_iteration   ]
    plt.plot(x, 'g^', x2, 'r--')

    file_name = "./figures/improvement-{}.png".format( len(stats_per_iteration ) )
    if os.path.exists(file_name):
        os.unlink(file_name)

    plt.savefig(file_name)


if __name__ == '__main__':

    pool_size = 128
    iterations = 1280
    new_brain_percent = .1

    brains = []
    iter = 0
    stats_per_iteration = []

    evolver = Evolver()

    while len(brains) < pool_size:
        brains.append( Brain() )

    for loop in range(iterations):
        plot(stats_per_iteration)
        iter += 1
        mutants = []
        while ( len(brains) + len(mutants) ) < pool_size:
            if random() < new_brain_percent:
                mutants.append(Brain())
            else:
                parent_brain = sample(brains, 1)[0]
                mutant = parent_brain.getNewMutant(mutation_chance=.2, max_mutation=.5)
                mutants.append( mutant )
        brains = brains + mutants
        shuffle(brains) # mix them up so winners don't always play winners first


        brains = evolver.find_top_brains(brains)

        # print ("***********************\n  Iteration {} winners\n***********************".format(iter))
        # for b in brains:
        #     print (b)

        print ("\n Iteration {} Stats\n***********************".format(iter))
        stats = evolver.getStats()
        stats_per_iteration.append(stats)
        for key in stats:
            print ("{} {}".format(key, stats[key]))





