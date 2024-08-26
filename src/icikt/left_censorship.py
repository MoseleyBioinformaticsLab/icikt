import numpy as np
from scipy.stats import binomtest
import typing as t
from icikt.utility import setupMissingMatrix


def leftCensorTest(dataArray: np.ndarray,
                   globalNA: t.List[float] = [float('nan'), float('inf'), 0],
                   sampleClasses: np.ndarray = None) -> dict:
    """ Does a binomial test to check if the most likely cause of missing values is due to values being below the limit
     of detection, or coming from a  left-censored distribution.

    :param dataArray: Numeric data to perform test on.
    :param globalNA: Optional list of values to be considered "missing". Default is NaN, Inf, and 0.
    :param sampleClasses: Which samples are in which class.
    :return: dict with values and binomtest results
    """
    # If sampleClasses not given, set everything to the same class 'A'
    if sampleClasses is None:
        sampleClasses = np.full(shape=len(dataArray), fill_value='A')

    # Split based on sampleClasses
    splitIndices = {cls: np.where(sampleClasses == cls)[0] for cls in set(sampleClasses.flat)}

    # Set up missingData matrix
    missingLoc = setupMissingMatrix(dataArray, globalNA)
    missingData = dataArray
    missingData[missingLoc] = float('nan')

    splitCounts = []
    for splitID, inSplit in splitIndices.items():
        splitMissing = missingData[:, inSplit - 1]
        nMiss = np.sum(np.isnan(splitMissing), axis=1)

        if np.sum(nMiss) == 0:
            splitCounts.append((0, 0, splitID))
            continue

        keepMiss = splitMissing[nMiss > 0, :]

        sampleMedians = calcMatrixMedians(splitMissing)

        medianMatrix = np.tile(sampleMedians, (keepMiss.shape[0], 1))
        keepMissUpDown = keepMiss < medianMatrix

        allTrials = np.prod(np.shape(keepMissUpDown)) - np.sum(np.isnan(keepMiss))
        allSuccess = np.nansum(keepMissUpDown)
        splitCounts.append((allTrials, allSuccess, splitID))

    totalTrials = int(sum(count[0] for count in splitCounts))
    totalSuccess = int(sum(count[1] for count in splitCounts))
    binomRes = binomtest(totalSuccess, totalTrials, p=0.5, alternative='greater')

    if sampleClasses is None:
        splitCounts = [(trials, success) for trials, success, _ in splitCounts]

    return {'values': splitCounts, 'binomialTest': binomRes}


def calcMatrixMedians(inMatrix: np.ndarray,
                      use: str = 'col',) -> np.ndarray:
    """ Calculate the median value of each row/col in inMatrix

    :param inMatrix: Input array of values.
    :param use: 'row' or 'col'. Default is 'col'.
    :return: Array of median values.
    """
    if use == 'row':
        inMatrix = inMatrix.T
    return np.nanmedian(inMatrix, axis=0)


# def addUniformNoise(val, nRep, sd, useZero=False):
#     nVal = len(val)
#     outSD = np.random.normal(0, sd, size=(nRep, nVal))
#     if not useZero:
#         tempVal = np.tile(val, (nRep, 1)).T
#         outVal = tempVal + outSD
#     else:
#         outVal = outSD
#
#     return outVal

