import numpy as np
import pandas as pd
import scipy.stats as sci


def runNumpyKT(x, y, type='global'):
    """Finds missing values, and replaces with a value slightly smaller than the minimum

    :param :class:'numpy.ndarray'x
    :param :class:'numpy.ndarray'y
    :param :py:class:'str'type
    """
    if type == 'local':
        x_na = pd.isnull(x)
        y_na = pd.isnull(y)
        match_na = x_na & y_na
        i = 0
        while i < len(match_na):
            if match_na[i]:
                x = np.delete(x, i)
                y = np.delete(y, i)
            i += 1

    min_xy = min(np.concatenate((x, y), axis=None)[np.concatenate((x, y), axis=None) != None])
    na_replace = min_xy - 0.1
    x2 = x
    y2 = y
    x2[pd.isnull(x)] = na_replace
    y2[pd.isnull(y)] = na_replace

    np_out = sci.kendalltau(x2,y2)
    print(np_out)


def main():
    """Created some test arrays to call runNumpyKT with
    """
    x = np.array([None, 5, 3, None, None, 2])
    y = np.array([4, 1, 17, 8, None, 6])
    runNumpyKT(x, y, 'local')


if __name__ == "__main__":
    main()

