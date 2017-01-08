#!/usr/bin/env python

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

The Artificial Bee Colony (ABC) algorithm is based on the
intelligent foraging behaviour of honey bee swarm, and was first proposed
by Karaboga in 2005.

"""

# ---- IMPORT MODULES

import math

try:
    import numpy as np
except:
    raise ImportError("Numpy module not installed.")

from Hive import Utilities
from Hive import Hive


# ---- CREATE TEST CASE

def evaluator(vector, a=1, b=100):
    """

    The Rosenbrock function is a non-convex function used as a performance test
    problem for optimization algorithms introduced by Howard H. Rosenbrock in
    1960. It is also known as Rosenbrock's valley or Rosenbrock's banana
    function.

    The function is defined by

                        f(x, y) = (a-x)^2 + b(y-x^2)^2

    It has a global minimum at (x, y) = (a, a**2), where f(x, y) = 0.

    """

    vector = np.array(vector)

    return (a - vector[0])**2 + b * (vector[1] - vector[0]**2)**2


# ---- SOLVE TEST CASE WITH ARTIFICIAL BEE COLONY ALGORITHM

def run():

    # creates model
    ndim = int(2)
    model = Hive.BeeHive(lower     = [0] *ndim ,
                         upper     = [10]*ndim ,
                         fun       = evaluator ,
                         numb_bees =  10       ,
                         max_itrs  =  50       ,)

    # runs model
    cost = model.run()

    # plots convergence
    Utilities.ConvergencePlot(cost)

    # prints out best solution
    print("Fitness Value ABC: {0}".format(model.best))


if __name__ == "__main__":
    run()


# ---- END
