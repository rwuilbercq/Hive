#!/usr/bin/env python

# ---- SELECTION METHODS

__all__ = ["tournament", "disruptive"]

# ---- MODULE DOCSTRING

__doc__ = """

(C) Hive, Romain Wuilbercq, 2017
     _
    /_/_      .'''.
 =O(_)))) ...'     `.
    \_\              `.    .'''X
                       `..'
.---.  .---..-./`) ,---.  ,---.   .-''-.
|   |  |_ _|\ .-.')|   /  |   | .'_ _   \
|   |  ( ' )/ `-' \|  |   |  .'/ ( ` )   '
|   '-(_{;}_)`-'`"`|  | _ |  |. (_ o _)  |
|      (_,_) .---. |  _( )_  ||  (_,_)___|
| _ _--.   | |   | \ (_ o._) /'  \   .---.
|( ' ) |   | |   |  \ (_,_) /  \  `-'    /
(_{;}_)|   | |   |   \     /    \       /
'(_,_) '---' '---'    `---`      `'-..-'

Description:
-----------

SelectionMethods.py

Defines a collection of selection methods to be used with Hive.

"""

# ---- IMPORT MODULES

import random

import numpy as np

# ---- SELECTION METHOD(S)

def tournament(values, crowd_size=None):
    """

    Defines a selection process whereby a number of individuals
    from a colony/generation are selected to compete.

    Individuals with greater fitness values compared to the rest
    have higher chance to be kept for the next cycle/generation
    - i.e. survival of the fittest. This method prones elitism.

    A solution compete with a fixed number of randomly chosen individuals
    (i.e. "crowd_size") from the population.

    This function uses the "random.sample" function from the python base
    "random" module and the "np.where" function from the "numpy" module.

    Parameters:
    ----------

        :param int crowd_size: number of individuals competing

    """

    # computes battle score metrics
    scores = []
    for i in range(len(values)):

        # selects a pool of opponents randomly
        if (crowd_size != None) and (type(crowd_size) is int):
            opponents = random.sample(values, crowd_size)
        else:
            opponents = values

        # battles against opponents
        scores.append( sum(np.where(values[i]>opponents, 1, 0)) )

    # returns an array of normalized scores
    return scores / sum(scores)

def disruptive(values):
    """

    Defines a selection process whereby a better chance is given to
    individuals with the highest and lowest fitness values - i.e. those
    further away from a "norm".

    This method represents a good mechanism by which diversity can
    be passed onto the next generation/cycle and avoid too-early
    convergence - i.e. improves the exploration of the search domain.

    This function uses the "np.mean" function from the "numpy" module.

    """

    # computes mean fitness of population
    mean_ = np.mean(values)

    # computes score metrics
    scores = []
    for i in range(len(values)):
        scores.append(abs(values[i] - mean_))

    # returns an array of normalized scores
    return scores / sum(scores)

# ---- END
