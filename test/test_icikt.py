import pytest as pt
import os
import icikt
import numpy as np


def test_icikt():
    # testing icikt submethod
    array = np.genfromtxt('./test/bigTest.csv', delimiter=",")

    x = array[:, 0]
    y = array[:, 1]

    # preserving the nan replacement done in iciktArray
    x[x == 0] = np.nan
    y[y == 0] = np.nan
    naReplaceX = np.nanmin(x) - 0.1
    naReplaceY = np.nanmin(y) - 0.1
    np.nan_to_num(x, copy=False, nan=naReplaceX)
    np.nan_to_num(y, copy=False, nan=naReplaceY)

    corr, pVal, tMax = icikt.icikt(x, y)
    corr, pVal, tMax = icikt.icikt(x, y, perspective='local')

    #testing iciktArray
    out, corr, pVal, tMax = icikt.iciktArray(dataArray=array, globalNA=[0], perspective="global", scaleMax=True, diagGood=True, includeOnly=None, chunkSize=1)


def test_error():
    array = np.genfromtxt('./test/bigTest.csv', delimiter=",")

    x = array[:-1, 0]
    y = array[:, 1]

    # preserving the nan replacement done in iciktArray
    x[x == 0] = np.nan
    y[y == 0] = np.nan
    naReplaceX = np.nanmin(x) - 0.1
    naReplaceY = np.nanmin(y) - 0.1
    np.nan_to_num(x, copy=False, nan=naReplaceX)
    np.nan_to_num(y, copy=False, nan=naReplaceY)

    try:
        corr, pVal, tMax = icikt.icikt(x, y)
    except ValueError:
        pass

