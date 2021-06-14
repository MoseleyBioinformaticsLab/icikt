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


def array_analysis(xyz):
    """Calls runNumpyKT to calculate ICI-Kendall-Tau between every combination of
    columns in the 2d array.

    :param :class:'numpy.ndarray'xyz
    :return: tuple of the correlations and pvalues 2d arrays
    """
    size = xyz.shape[1]
    correlations, pvalues = np.zeros([size, size]), np.zeros([size, size])

    # produces every combination of columns in the array
    product = it.product(np.hsplit(xyz, size), np.hsplit(xyz, size))
    # calls runNumpyKT to calculate ICIKendallTau for every combination in product and stores in a list
    tempList = [runNumpyKT(np.squeeze(i[0]), np.squeeze(i[1]), 'local') for i in product]

    # separates+stores the correlation & pvalue data from every combination at the correct location in the output arrays
    length = int(len(tempList)/size)
    for a in range(length):
        for i in range(size):
            correlations[a, i] = tempList[i + a * size][0]
            pvalues[a, i] = tempList[i + a * size][1]

    return correlations, pvalues


def main():
    """Created some test arrays to call runNumpyKT with
    """
    x = np.array([np.nan, 5, 3, np.nan, np.nan, 2])
    y = np.array([4, 1, 17, 8, np.nan, 6])
    z = np.array([6, 10, np.nan, 3, 9, 14])
    xyz = np.column_stack((x, y, z))
    # runNumpyKT(x, y, 'local')
    corr, pval = array_analysis(xyz)
    print(corr)
    print(pval)


if __name__ == "__main__":
    main()
