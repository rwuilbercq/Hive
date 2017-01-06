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

try:
    import numpy as np
except:
    raise ImportError("Numpy module not installed.")

from Hive import Hive
from Hive import Utilities

# ---- CREATE TEST CASE

def evaluator(vector):
    """
    A n-dimensional Rastrigin's function is defined as:

                            n
            f(x) = 10*n + Sigma { x_i^2 - 10*cos(2*PI*x_i) }
                           i=1

    where  -5.12 <= x_i <= 5.12.

    Thus the global minima of the function being f(x) = 0 at all x_i = 0.

    """

    vector = np.array(vector)

    return 10 * vector.size + sum(vector*vector - 10 * np.cos(2 * np.pi * vector))


# ---- SOLVE TEST CASE WITH ARTIFICIAL BEE COLONY ALGORITHM

def run():

    # creates model
    ndim = int(10)
    model = Hive.BeeHive(lower = [-5.12]*ndim  ,
                         upper = [ 5.12]*ndim  ,
                         fun       = evaluator ,
                         numb_bees =  50       ,
                         max_itrs  =  100       ,)

    # runs model
    cost = model.run()

    # plots convergence
    Utilities.ConvergencePlot(cost)

    # prints out best solution
    print("Fitness Value ABC: {0}".format(model.best))


if __name__ == "__main__":
    run()


# ---- END
