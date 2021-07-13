"""
Python Information-Content-Informed Kendall Tau Correlation (pyICIKT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Usage:
    kendalltau.py iciktArray <2dArray> [<replaceValue>] <type>
    kendalltau.py -h | --help

Options:
    -h, --help                          Shows this screen.
"""


import numpy as np
import scipy.stats as sci
import itertools as it
import time
import multiprocessing
import docopt


def iciKT(x, y, type='global'):
    """Finds missing values, and replaces them with a value slightly smaller than the minimum between both arrays.

    :param x: First array of data
    :type x: :class:`numpy.ndarray`
    :param y: Second array of data
    :type y: :class:`numpy.ndarray`
    :param type: type can be 'local' or 'global'. Default is 'global'.  Global includes (NA,NA) pairs in the calculation, while local does not.
    :type type: :py:class:`str`
    :return: List with correlation and pvalue
    :rtype: :py:class:`list`
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


def iciktArray(dataArray, replaceVal=None, type='global'):
    """Calls iciKT to calculate ICI-Kendall-Tau between every combination of
    columns in the input 2d array, dataArray. Also replaces any instance of the replaceVal in the array with np.nan.

    :param dataArray: 2d array with columns of data to analyze
    :type dataArray: :class:`numpy.ndarray`
    :param replaceVal: Optional value to replace with np.nan. Default is None.
    :type replaceVal: :py:class:`int` or :py:class:`float` or :class:`None`
    :param type: type can be 'local' or 'global'. Default is 'global'.  Global includes (NA,NA) pairs in the calculation, while local does not.
    :type type: :py:class:`str`
    :return: tuple of the correlations and pvalues 2d arrays
    :rtype: :py:class:`tuple`
    """

    if replaceVal is not None:
        dataArray[dataArray == replaceVal] = np.nan

    size = dataArray.shape[1]
    corrArray, pvalArray = np.zeros([size, size]), np.zeros([size, size])

    # produces every combination of columns in the array
    product = it.product(np.hsplit(dataArray, size), np.hsplit(dataArray, size))

    # calls iciKT to calculate ICIKendallTau for every combination in product and stores in a list
    with multiprocessing.Pool() as pool:
        tempList = pool.starmap(iciKT, ((*i, type) for i in product))

    # separates+stores the correlation & pvalue data from every combination at the correct location in the output arrays
    length = int(len(tempList)/size)
    for a in range(length):
        for i in range(size):
            corrArray[a, i] = tempList[i + a * size][0]
            pvalArray[a, i] = tempList[i + a * size][1]

    return corrArray, pvalArray


def main(args):
    # make options for csv or tab-delimited file
    if args["iciktArray"]:
        args["<2dArray>"] = np.genfromtxt(args["<2dArray>"], delimiter=',')
        if args["replaceValue"] != "None":
            args["replaceValue"] = float(args["replaceValue"])
        iciktArray(args["<2dArray>"], args["<replaceValue>"], args["<type>"])



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
    args = docopt.docopt(__doc__)
    main(args)


