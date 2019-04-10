import numpy as np


def gini_coeff(values_arg):
    """
    Modified from wikixray/graphics.py:70
    (For instance see github mirror here: https://github.com/ryanwitt/wikixray/blob/master/graphics.py)
    Plots a Gini graph for author values.

    @type  values: a Python list or np.array of numbers to calculate gini coefficient on
    """

    values = np.array(values_arg)

    n_users = len(values) # n_users => n + 1

    values.sort() # sort in-place in ascending order

    sum_numerator=0
    sum_denominator=0
    for i in range(1, n_users):
        sum_numerator += (n_users-i) * values[i]
        sum_denominator += values[i]
    if sum_denominator == 0:
        return np.NaN

    # Using this formula: https://github.com/Grasia/WikiChron/wiki/assets/gini.png
    g_coeff = n_users-2*(sum_numerator/sum_denominator)

    # Now, apply (Deltas, 2003 correction) for small datasets:
    # (https://doi.org/10.1162/rest.2003.85.1.226)
    g_coeff *= (1.0 / (n_users - 2))

    return g_coeff
