from typing import Union, List
import numpy as np

def theil(values_arg: Union[List, np.array], n=None):
    """
    Calculates de Theil index using the formula shown in assets/theil_formula.png

    @type values: a Pyhon list or np.array of numbers to calculate gini coefficient on
    """
    if n is None:
        n = len(values_arg)

    values = np.array(values_arg)
    mu = np.average(values)

    if mu == 0 or n == 0:
        return np.NaN

    sum = 0

    for xi in values:
        if xi == 0: 
            # xi * 0 = 0, it doesn't add anything to the sum
            continue

        div = xi / mu
        sum += div * np.log(div)

    theil_coeff = sum / n
    return theil_coeff