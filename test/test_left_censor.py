# import icikt.__main__ as cli
import pytest as pt
import os
import icikt
import numpy as np


# @pt.mark.parametrize('argv', test_data)
def test_leftCensor():
    test_data = np.genfromtxt('/mlab/scratch/rmflight/praneeth/largish_sample.tsv', delimiter='\t')
    results = icikt.leftCensorTest(test_data)
