import numpy as np
import scipy.stats as sci
import itertools as it
import time
import multiprocessing
import sys


def iciKT(x, y, type='global'):
    """Finds missing values, and replaces them with a value slightly smaller than the minimum between both arrays.

    :param x: First array of data
    :type x: np.ndarray
    :param y: Second array of data
    :type y: np.ndarray
    :param type: Default is 'global'
    :type type: str
    :return: List with correlation and pvalue
    :rtype: :py:class:'list'
    """

    if type == 'local':
        matchNA = np.logical_and(np.isnan(x), np.isnan(y))
        x = x[np.logical_not(matchNA)]
        y = y[np.logical_not(matchNA)]

    naReplace = min(np.fmin(x, y)) - 0.1
    np.nan_to_num(x, copy=False, nan=naReplace)
    np.nan_to_num(y, copy=False, nan=naReplace)

    corr, pval = sci.kendalltau(x, y)
    return [corr, pval]


def iciktArray(dataArray, replaceVal=None):
    """Calls iciKT to calculate ICI-Kendall-Tau between every combination of
    columns in the input 2d array, dataArray. Also replaces any instance of the replaceVal in the array with np.nan.

    :param dataArray: 2d array with columns of data to analyze
    :type dataArray: np.ndarray
    :param replaceVal: Optional value to replace with np.nan. Default is None.
    :type replaceVal: int or float or None
    :return: tuple of the correlations and pvalues 2d arrays
    :rtype: :py:class:'tuple'
    """

    if replaceVal is not None:
        dataArray[dataArray == replaceVal] = np.nan

    size = dataArray.shape[1]
    corrArray, pvalArray = np.zeros([size, size]), np.zeros([size, size])

    # produces every combination of columns in the array
    product = it.product(np.hsplit(dataArray, size), np.hsplit(dataArray, size))

    # calls iciKT to calculate ICIKendallTau for every combination in product and stores in a list
    with multiprocessing.Pool() as pool:
        tempList = pool.starmap(iciKT, ((*i, 'local') for i in product))

    # separates+stores the correlation & pvalue data from every combination at the correct location in the output arrays
    length = int(len(tempList)/size)
    for a in range(length):
        for i in range(size):
            corrArray[a, i] = tempList[i + a * size][0]
            pvalArray[a, i] = tempList[i + a * size][1]

    return corrArray, pvalArray


def main():
    bigTest()


def smallTest():

    x = np.array([np.nan, 5, 3, np.nan, np.nan, 2])
    y = np.array([4, 0, 17, 8, np.nan, 6])
    z = np.array([6, 10, np.nan, 3, 9, 14])
    xyz = np.column_stack((x, y, z))

    sTime = time.time()
    corr, pval = iciktArray(xyz, replaceVal=0)
    fTime = time.time()

    print(corr)
    print(pval)
    print(fTime - sTime)


def bigTest():

    largeArray = np.genfromtxt('/mlab/data/psbhatt/projects/pythonICIKendallTau/pyicikendalltau/bigTest.csv', delimiter=",")

    sTime = time.time()
    corr, pval = iciktArray(largeArray)
    fTime = time.time()

    print(corr)
    print(pval)
    print(fTime - sTime)


if __name__ == "__main__":
    main()
