"""Possible functional forms that can be used in system dynamics modelling."""

import numpy as np


def sigmoid(x, height=1, base=0, shift=0.5, slope=10):
    """Sigmoidal function that, using default values is bounded between [0,1] for both axes.

    Parameters
    ----------
    x :
        
    height :
         (Default value = 1)
    base :
         (Default value = 0)
    shift :
         (Default value = 0.5)
    slope :
         (Default value = 10)

    Returns
    -------

    """
    return base + (height * (1 / (1 + np.exp((-x + shift) * slope))))


def linear(x, a=1, b=0):
    """Linear function.

    Parameters
    ----------
    x :
        
    a :
         (Default value = 1)
    b :
         (Default value = 0)

    Returns
    -------

    """
    return a * x + b
