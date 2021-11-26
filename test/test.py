import numpy as np
import time

import sys
# inserting icikt path
sys.path.insert(1, '/mlab/data/psbhatt/projects/pythonICIKendallTau/icikt')
import icikt


def iciKTTest():
    largeArray = np.genfromtxt('/mlab/data/psbhatt/projects/pythonICIKendallTau/test/bigTest2.tab.csv', delimiter="\t")

    x = largeArray[:, 0]
    y = largeArray[:, 1]
    x[x == 0] = np.nan
    y[y == 0] = np.nan
    naReplaceX = np.nanmin(x) - 0.1
    naReplaceY = np.nanmin(y) - 0.1
    np.nan_to_num(x, copy=False, nan=naReplaceX)

    sTime = time.time()
    corr, pVal, tMax = icikt.iciKT(x, y)
    fTime = time.time()

    print(*(corr, pVal, tMax), sep="\n")
    print("Runtime: ", fTime - sTime)


def iciktArrayTest():
    largeArray = np.genfromtxt('/mlab/data/psbhatt/projects/pythonICIKendallTau/test/bigTest2.tab.csv', delimiter="\t")

    sTime = time.time()
    out, corr, pVal, tMax = icikt.iciktArray(largeArray)
    fTime = time.time()

    print(*(out, corr, pVal, tMax), sep="\n")
    print("Runtime: ", fTime - sTime)
