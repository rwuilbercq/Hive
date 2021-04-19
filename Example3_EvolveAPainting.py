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

Description:
-----------

This example shows how to evolve a famous painting using polygons.

The location of a number of polygons and RGB colors are evolved by an Artificial
Bee Colony algorithm to replicate a famous painting from Henri Matisse.

This example is inspired by a blog post written by Roger Alsing.

Reference:
---------

http://rogeralsing.com/2008/12/07/genetic-programming-evolution-of-mona-lisa/

Dependencies:
------------

- PIL
- sklearn-image
- numpy
- matplotlib

"""

# ---- IMPORT MODULES

# import internal modules

from Hive import Hive

# import external modules

import numpy as np

from sklearn.metrics import mean_squared_error as mse

try:
    from PIL import ImageChops, Image
except:
    raise ImportError("PIL module not found.")

try:
    import matplotlib.path as mpath
    import matplotlib.pyplot as plt
    import matplotlib as mpl
except:
    raise ImportError("matplotlib module not found.")

try:
    from skimage import color
except:
    raise ImportError("sklearn-image module not found.")

# ---- PROCESS IMAGE

# loads original image
source_image = Image.open("assets/matisse.jpg")
xsize, ysize = source_image.size

# post-processes source image as a np.ndarray
SOURCE_IMAGE = np.array(source_image)

# defines size of image [pixels/inch]
dpi = 80

# converts image to gray scale
source_image_gray = color.rgb2gray(SOURCE_IMAGE)

# ---- DEFINE BLANK CANVAS

# define image polygons parameters
nb_polygons, nb_pts_per_polygon, nb_rgb = 8, 4, 3

def polygon(x, y, up=1):
    """ Creates a polygon. """

    # defines vertex coordinates of a dummy polygon "path"
    vertices = [(x[0], y[0]), (x[1], y[1]),
                (x[2], y[2]), (x[3], y[3]),
                (x[0], y[0])                ]

    # creates a polygon
    poly = mpath.Path(vertices, [mpath.Path.MOVETO] + \
           (len(vertices)-1) * [mpath.Path.LINETO])

    # returns polygon
    return poly

def create_image(vector):
    """ Creates an image from a set of polygons. """

    # converts vector input to numpy.ndarray
    vector = np.array(vector)

    # creates a list of shapes and colors
    shapes = []; colors = [];
    for ix in range(nb_polygons):

        # processes input vector - "unrolling" vector
        ind_start_x = ix * (nb_pts_per_polygon * 2 + 3)
        ind_start_y = ind_start_x + 4
        ind_start_c = ind_start_y + 4
        x = vector[ind_start_x : ind_start_y]
        y = vector[ind_start_y : ind_start_c]
        color = vector[ind_start_c : ind_start_c + 3]

        # creates list of polygons and colors
        shapes.append(polygon(x*xsize, y*ysize))
        colors.append([color[i] for i in range(3)])

    # creates a figure of the same dimension as source image
    fig, ax = plt.subplots(figsize=(xsize/dpi, ysize/dpi), dpi=dpi)
    ax.set_rasterization_zorder(1)

    # creates a collection of polygonal shapes
    set_of_shapes = mpl.collections.PathCollection(shapes,
                                                   facecolor=colors,
                                                   linewidth=0)

    # creates an image
    ax.add_collection(set_of_shapes)
    ax.set_frame_on(False)
    ax.axis('off')
    ax.autoscale_view()

    # draws image
    fig.tight_layout(pad=0)
    fig.canvas.draw()

    # converts image to np.ndarray
    data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
    image = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    # returns image array
    return image


# ---- CREATE EVALUATOR

def compare_images_mse(source_image, new_image):
    """ Computes the root mean-square. """

    err = np.sum((source_image.astype("float") - new_image.astype("float")) ** 2)
    err /= float(source_image.shape[0] * source_image.shape[1])

    return err

def evaluator(vector):
    """ Computes similarity between newly created and source image. """

    # creates an image
    image = create_image(vector)

    # closes current figure
    plt.close()

    # compare new image with source image
    return compare_images_mse(SOURCE_IMAGE, image)


# ---- SOLVE TEST CASE

def run():

    # creates model
    ndim = int(nb_polygons * (2 * nb_pts_per_polygon + nb_rgb))
    model = Hive.BeeHive(lower     = [0]*ndim   ,
                         upper     = [1]*ndim   ,
                         fun       = evaluator  ,
                         numb_bees = 20         ,
                         max_itrs  = 1000       ,
                         verbose   = True       ,)

    # runs model
    model.run()

    # saves an image of the end result
    solution = create_image(model.solution)
    plt.savefig('solutionMatisse.png', bbox_inches='tight')


if __name__ == "__main__":
    run()


# ---- END
