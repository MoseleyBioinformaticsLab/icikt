import pytest as pt
import icikt
import numpy as np


def test_leftCensor():
    test_data = np.genfromtxt('./test/small_sample.tsv', delimiter='\t')
    try:
        results = icikt.leftCensorTest(test_data)
    except Exception:
        pt.fail("Error")
