import numpy as np


def gini(values_arg, n = None):
    """
    Calculates the gini_coeff using the formula shown in assets/gini_formula.png

    Remind that len(values) here corresponds to n+1 there in that formula and remind that idx here corresponds to i-1 in the formula,
    since python lists are zero-indexed and the formula is one-indexed
    this can be confusing.

    @type  values: a Python list or np.array of numbers to calculate gini coefficient on
    """

    if n is None:
        n = len(values_arg)

    values = np.array(values_arg)

    values.sort() # sort in-place in ascending order

    sum_numerator = 0
    sum_denominator = 0
    for idx in range(0, n):
        i = idx + 1 # idx here corresponds to i-1 in the formula, since python lists are zero-indexed
        sum_numerator += (n + 1 - i) * values[idx]
        sum_denominator += values[idx]
    if sum_denominator == 0:
        return np.NaN

    g_coeff = n + 1 - 2*(sum_numerator/sum_denominator)

    return g_coeff


def gini_corrected(values_arg, n = None):
    """
    Calculates the gini_coeff with a correction for small datasets

    @type  values: a Python list or np.array of numbers to calculate gini coefficient on
    """

    if n is None:
        n = len(values_arg)

    if n < 2: # Don't calculaute Gini for populations with less than one individual
        return np.NaN

    # compute gini coefficient
    g_coeff = gini(values_arg, n)

    # Now, apply (Deltas, 2003 correction) for small datasets:
    # (https://doi.org/10.1162/rest.2003.85.1.226)
    g_coeff *= (1.0 / (n - 1))

    return g_coeff
