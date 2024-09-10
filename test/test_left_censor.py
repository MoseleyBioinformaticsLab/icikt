import pytest as pt
import icikt
import numpy as np


def test_leftCensor():
    test_data = np.genfromtxt('./test/example_left_missing.csv', delimiter=',', skip_header = 1)
    binomial_res, values = icikt.leftCensorTest(test_data)
    assert binomial_res.statistic == 0.8
