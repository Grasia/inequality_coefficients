import math
import numpy as np

def ratio_top_rest(values_arg, percentage):
    """
    Implements this formula: https://github.com/Grasia/WikiChron/wiki/assets/ratio_10_90.png

    Input can be np.array or list of numbers.
    """

    percentage_top = percentage * 0.01
    values = np.array(values_arg)

    values.sort() # sort in-place in ascending order

    n_users = len(values)
    #~ top_percent_users would be = math.ceil(n_users * percentage_top);
    rest_users = math.floor(n_users * (1 - percentage_top));
    edits_rest = values[:rest_users].sum()
    edits_top  = values[rest_users:].sum()

    return (edits_top / edits_rest)


def ratio_top10_rest(values_arg):
    return ratio_top_rest(values_arg, 10)
