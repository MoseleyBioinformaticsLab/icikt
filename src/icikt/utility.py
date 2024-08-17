import numpy as np
import typing as t

def setupMissingMatrix(dataArray: np.ndarray,
                       globalNA: t.List = [float("nan"), float("inf"), 0]) -> np.ndarray:
    """ Used by iciktArray and leftCensorTest to set up the matrix of values marking which should be excluded.

    :param dataArray: 2d array with columns of data to analyze
    :param globalNA: Optional list of values to be considered "missing". Default is NaN, Inf, and 0.
    :return: 2d array with locations of values to exclude
    """

    # create an empty array to store exclude locations
    excludeLoc = np.full(shape=dataArray.shape, fill_value=False, dtype=bool)
    # For each value in globalNA, mark those values in excludeLoc as True
    for val in globalNA:
        if np.isnan(val):
            excludeLoc[np.isnan(dataArray)] = True
        elif np.isinf(val):
            excludeLoc[np.isinf(dataArray)] = True
        else:
            excludeLoc[dataArray == val] = True

    return excludeLoc
