import numpy as np
import scipy.stats as sci


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

    np_out = sci.kendalltau(x, y)
    print(np_out)


def main():
    """Created some test arrays to call runNumpyKT with
    """
    x = np.array([np.nan, 5, 3, np.nan, np.nan, 2])
    y = np.array([4, 1, 17, 8, np.nan, 6])
    runNumpyKT(x, y, 'local')


if __name__ == "__main__":
    main()
