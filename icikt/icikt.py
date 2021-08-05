"""
Python Information-Content-Informed Kendall Tau Correlation (ICIKT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""



import numpy as np
import scipy.stats as sci
import itertools as it
import time
import multiprocessing


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


def iciktArray(dataArray, globalNA=None, type='global'):
    """Calls iciKT to calculate ICI-Kendall-Tau between every combination of
    columns in the input 2d array, dataArray. Also replaces any instance of the globalNA in the array with np.nan.

    :param dataArray: 2d array with columns of data to analyze
    :type dataArray: :class:`numpy.ndarray`
    :param globalNA: Optional value to replace with np.nan. Default is None.
    :type globalNA: :py:class:`float` or :class:`None`
    :param type: type can be 'local' or 'global'. Default is 'global'.  Global includes (NA,NA) pairs in the calculation, while local does not.
    :type type: :py:class:`str`
    :return: tuple of the correlations and pvalues 2d arrays
    :rtype: :py:class:`tuple`

    Future Parameters:
    featureNA
    sampleNA
    scaleMax
    diagGood

    """

    if globalNA is not None:
        dataArray[dataArray == globalNA] = np.nan

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

    print(corrArray)
    print(pvalArray)
    return corrArray, pvalArray



