import numpy as np
import scipy.stats as sci
import itertools as it


def runNumpyKT(x, y, type='global'):
    """Finds missing values, and replaces them with a value slightly smaller than the minimum between both arrays.

    :param :class:'numpy.ndarray'x
    :param :class:'numpy.ndarray'y
    :param :py:class:'str'type
    """
    if type == 'local':
        match_na = np.logical_and(np.isnan(x), np.isnan(y))
        x = x[np.logical_not(match_na)]
        y = y[np.logical_not(match_na)]

    na_replace = min(np.fmin(x, y)) - 0.1
    np.nan_to_num(x, copy=False, nan=na_replace)
    np.nan_to_num(y, copy=False, nan=na_replace)

    corr, pval = sci.kendalltau(x, y)
    return [corr, pval]


def arrayanalysis(xyz):
    """Iterates over the columns of data and calls runNumpyKT on them to find data.

    :param :class:'numpy.ndarray'xyz
    """
    correlations, pvalues = np.zeros([xyz.shape[1], xyz.shape[1]]), np.zeros([xyz.shape[1], xyz.shape[1]])

    product = it.product(np.hsplit(xyz, xyz.shape[1]), np.hsplit(xyz, xyz.shape[1]))
    tempList = [runNumpyKT(np.squeeze(i[0]), np.squeeze(i[1]), 'local') for i in product]

    length = int(len(tempList)/xyz.shape[1])
    for a in range(length):
        for i in range(xyz.shape[1]):
            correlations[a, i] = tempList[i+a*(xyz.shape[1])][0]
            pvalues[a, i] = tempList[i+a*(xyz.shape[1])][1]

    print(correlations)
    print(pvalues)


def main():
    """Created some test arrays to call runNumpyKT with
    """
    x = np.array([np.nan, 5, 3, np.nan, np.nan, 2])
    y = np.array([4, 1, 17, 8, np.nan, 6])
    z = np.array([6, 10, np.nan, 3, 9, 14])
    xyz = np.column_stack((x, y, z))
    # runNumpyKT(x, y, 'local')
    arrayanalysis(xyz)


if __name__ == "__main__":
    main()
