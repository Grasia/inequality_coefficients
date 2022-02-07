import numpy as np
import pytest

from inequality_coefficients import gini
from ineq.indexes import gini as gini_test  # to test gini against


def test_gini():
    a = np.random.choice(100, 100)
    g = gini_test(a)*100
    g_test = gini(a)

    assert pytest.approx(g) == g_test


def test_gini_decimal():
    a = np.random.rand(100) * 100
    g = gini_test(a)*100
    g_test = gini(a)

    assert pytest.approx(g) == g_test
