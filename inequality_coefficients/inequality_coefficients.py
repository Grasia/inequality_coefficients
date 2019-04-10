import numpy as np


def ratio_top_rest(values, percentage):
    """
    Implements this formula: https://github.com/Grasia/WikiChron/wiki/assets/ratio_10_90.png
    """

    percentage_top = percentage * 0.01

    sorted_values = sorted(values, reverse=False)

    top_percent_users = math.ceil(n_users * percentage_top);
    #~ rest_users would be = floor(n_users * (1 - percentage_top));
    edits_top = sorted_values[:top_percent_users].sum()
    edits_rest = sorted_values[top_percent_users:].sum()

    return edits_top / edits_rest


def ratio_top10_rest(values):
    return ratio_top_rest(values, 10)


def gini_coeff(values):
    """
    Modified from wikixray/graphics.py:70
    (For instance see github mirror here: https://github.com/ryanwitt/wikixray/blob/master/graphics.py)
    Plots a Gini graph for author values.

    @type  values: a list of numbers to calculate gini coefficient for
    """

    n_users = len(values) # n_users => n + 1

    sorted_values = sorted(values)

    sum_numerator=0
    sum_denominator=0
    for i in range(1, n_users):
        sum_numerator += (n_users-i) * values[i]
        sum_denominator += sorted_values[i]
    if sum_denominator == 0:
        return np.NaN

    # Using this formula: https://github.com/Grasia/WikiChron/wiki/assets/gini.png
    g_coeff = n_users-2*(sum_numerator/sum_denominator)

    # Now, apply (Deltas, 2003 correction) for small datasets:
    # (https://doi.org/10.1162/rest.2003.85.1.226)
    g_coeff *= (1.0 / (n_users - 2))

    return g_coeff
