import numpy as np
import scipy.stats as sci
import itertools as it
import time
import multiprocessing


def iciKT(x, y, type='global'):
    """Finds missing values, and replaces them with a value slightly smaller than the minimum between both arrays.

    :param :class:'numpy.ndarray'x
    :param :class:'numpy.ndarray'y
    :param :py:class:'str'type: Default is 'global'.
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

    :param :class:'numpy.ndarray'dataArray
    :param replaceVal: Optional value to replace with np.nan. Default is None.
    :type replaceVal: :py:class:'NoneType.None' or :py:class:'int' or :py:class:'double' or py:class:'float'
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
    """Created some test arrays to call runNumpyKT with
    """

    largeArray = np.genfromtxt('D:/large_transcript.csv', delimiter=",")
    tmpArray = largeArray[..., :50]

    sTime = time.time()
    corr, pval = iciktArray(tmpArray, replaceVal=0)
    fTime = time.time()

    print(corr)
    print(pval)
    print(fTime - sTime)


if __name__ == "__main__":
    main()
