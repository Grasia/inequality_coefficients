import numpy as np
import pytest

from inequality_coefficients import theil

def test_theil():
    # Random array
    # Result calculated using a spreadsheet
    test_array = np.array([
        0.88534692, 0.14636409, 0.57989106, 0.90247583, 0.89786841,
        0.34349194, 0.89998219, 0.53715335, 0.78262043, 0.13758317])

    assert pytest.approx(theil(test_array)) == 0.139688731917064
