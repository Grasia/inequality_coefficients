import numpy as np

from inequality_coefficients import gini
from ineq.indexes import gini as gini_test  # to test gini against


def test_gini():
    a = np.random.choice(100, 100)
    g = gini_test(a)
    g_test = gini(a)

    assert g, g_test


def test_gini_decimal():
    a = np.random.rand(100) * 100
    g = gini_test(a)
    g_test = gini(a)

    assert g, g_test
