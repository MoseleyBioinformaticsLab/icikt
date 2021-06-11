import numpy as np
import scipy.stats as sci


def runNumpyKT(x, y, type='global'):
    """Finds missing values, and replaces with a value slightly smaller than the minimum

    :param :class:'numpy.ndarray'x
    :param :class:'numpy.ndarray'y
    :param :py:class:'str'type
    """
    if type == 'local':
        x_na = np.isnan(x)
        y_na = np.isnan(y)
        match_na = x_na & y_na
        i = 0
        while i < len(match_na):
            if match_na[i]:
                x = np.delete(x, i)
                y = np.delete(y, i)
            i += 1
    xy = np.concatenate((x, y), axis=None)
    na_replace = min(xy[~np.isnan(xy)]) - 0.1
    x2 = x
    y2 = y
    x2[np.isnan(x)] = na_replace
    y2[np.isnan(y)] = na_replace

    np_out = sci.kendalltau(x2, y2)
    print(np_out)


def main():
    """Created some test arrays to call runNumpyKT with
    """
    x = np.array([np.nan, 5, 3, np.nan, np.nan, 2])
    y = np.array([4, 1, 17, 8, np.nan, 6])
    runNumpyKT(x, y, 'local')


if __name__ == "__main__":
    main()
