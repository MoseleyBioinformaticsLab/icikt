import pytest as pt
import os
import icikt
import numpy as np
import sys

test_data = [
    'global',
    'local'
]


@pt.mark.parametrize('persp', test_data)
def test_icikt(persp):
    # testing icikt submethod
    array = np.genfromtxt('./test/small_sample.csv', delimiter=",")

    x = array[:, 0]
    y = array[:, 1]

    # preserving the nan replacement done in iciktArray
    x[x == 0] = np.nan
    y[y == 0] = np.nan
    naReplaceX = np.nanmin(x) - 0.1
    naReplaceY = np.nanmin(y) - 0.1
    np.nan_to_num(x, copy=False, nan=naReplaceX)
    np.nan_to_num(y, copy=False, nan=naReplaceY)

    try:
        corr, pVal, tMax = icikt.icikt(x, y, perspective=persp)
    except Exception:
        pt.fail("Error")


def test_iciktArray():
    # testing icikt submethod
    array = np.genfromtxt('./test/small_sample.csv', delimiter=",")

    # testing iciktArray
    try:
        out, corr, pVal, tMax = icikt.iciktArray(dataArray=array, globalNA=[0])
    except Exception:
        pt.fail("Error")


def test_error():
    array = np.genfromtxt('./test/small_sample.csv', delimiter=",")

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
