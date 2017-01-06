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

# ---- IMPORT MODULE(S)
from distutils.core import setup

# ---- SETUP INFORMATION
setup(name         = "Hive",
      version      = "x.x.x",
      description  = "Artificial Bee Colony Algorithm",
      author       = "Romain Wuilbercq",
      author_email = "romain.wuilbercq@gmail.com",
      url          = "https://github.com/rwuilbercq/Forest",
      keywords     = ["optimisation", "swarm", "stochastic", "global"],
      classifiers  = [
          "Programming Language :: Python",
          "Development Status :: Beta",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3"
      ],
      long_description = """

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

      """)
