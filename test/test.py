import numpy as np
import time

import sys
# inserting icikt path
sys.path.insert(1, '/mlab/data/psbhatt/projects/pythonICIKendallTau/icikt')
import icikt


def iciKTTest(array):

    x = array[:, 0]
    y = array[:, 1]

    # preserving the nan replacement done in iciktArray
    x[x == 0] = np.nan
    y[y == 0] = np.nan
    naReplaceX = np.nanmin(x) - 0.1
    naReplaceY = np.nanmin(y) - 0.1
    np.nan_to_num(x, copy=False, nan=naReplaceX)
    np.nan_to_num(y, copy=False, nan=naReplaceY)

    sTime = time.time()
    corr, pVal, tMax = icikt.iciKT(x, y)
    fTime = time.time()

    print(corr, pVal, tMax, sep="\n")
    print("Runtime: ", fTime - sTime)


def iciktArrayTest(array):

    sTime = time.time()
    out, corr, pVal, tMax = icikt.iciktArray(array)
    fTime = time.time()

    print(out, corr, pVal, tMax, sep="\n")
    print("Runtime: ", fTime - sTime)


largeArray = np.genfromtxt('/mlab/data/psbhatt/projects/icikt/test/bigTest.csv', delimiter=",")
# iciKTTest(largeArray)
iciktArrayTest(largeArray)
