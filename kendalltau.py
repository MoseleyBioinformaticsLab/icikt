import numpy as np
import scipy.stats as sci
import itertools as it
import time
import multiprocessing


def iciKT(x, y, type='global'):
    """Finds missing values, and replaces them with a value slightly smaller than the minimum between both arrays.

    :param :class:'numpy.ndarray'x
    :param :class:'numpy.ndarray'y
    :param :py:class:'str'type
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


def iciktArray(xyz, replaceVal=None):
    """Calls runNumpyKT to calculate ICI-Kendall-Tau between every combination of
    columns in the 2d array.

    :param :class:'numpy.ndarray'xyz
    :return: tuple of the correlations and pvalues 2d arrays
    """
    if replaceVal is not None:
        xyz[xyz == replaceVal] = np.nan

    size = xyz.shape[1]
    corrArray, pvalArray = np.zeros([size, size]), np.zeros([size, size])

    # produces every combination of columns in the array
    product = it.product(np.hsplit(xyz, size), np.hsplit(xyz, size))
    # calls runNumpyKT to calculate ICIKendallTau for every combination in product and stores in a list

    # tempList = [iciKT(np.squeeze(i[0]), np.squeeze(i[1]), 'local') for i in product]

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
    # x = np.array([np.nan, 5, 3, np.nan, np.nan, 2])
    # y = np.array([4, 0, 17, 8, np.nan, 6])
    # z = np.array([6, 10, np.nan, 3, 9, 14])
    # xyz = np.column_stack((x, y, z))
    # runNumpyKT(x, y, 'local')
    # corr, pval = iciktArray(xyz, replaceVal=6)
    largeArray = np.genfromtxt('D:/large_transcript.csv', delimiter=",")
    tmpArray = largeArray[..., 0:50]

    sTime = time.time()
    corr, pval = iciktArray(tmpArray, replaceVal=0)
    fTime = time.time()

    print(corr)
    print(pval)
    print(fTime - sTime)


if __name__ == "__main__":
    main()
