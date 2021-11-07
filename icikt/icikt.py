"""
Python Information-Content-Informed Kendall Tau Correlation (ICIKT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The pythonICIKendallTau package provides a Python tool to calculate an
information-content-informed Kendall Tau correlation coefficient between
arrays, while also handling missing values or values which need to be removed.
"""

import numpy as np

from scipy.stats import mstats_basic
from scipy.stats import distributions

import itertools as it
import multiprocessing

import pyximport

pyximport.install()
from kendall_dis import _kendall_dis


def iciKT(x, y, perspective='global'):
    """Finds missing values, and replaces them with a value slightly smaller than the minimum between both arrays.

    :param x: First array of data
    :type x: :class:`numpy.ndarray`
    :param y: Second array of data
    :type y: :class:`numpy.ndarray`
    :param perspective: perspective can be 'local' or 'global'. Default is 'global'.  Global includes (NA,NA) pairs in the calculation, while local does not.
    :type perspective: :py:class:`str`
    :return: tuple with correlation, pvalue, and tauMax values
    :rtype: :py:class:`tuple`
    """

    def countRankTie(ranks):
        """Counts rank ties.

        :param ranks: input array
        :type ranks: :class:`numpy.ndarray`
        :return: tuple of int sums
        :rtype: :py:class:`tuple`
        """
        count = np.bincount(ranks).astype('int64', copy=False)
        count = count[count > 1]

        return ((count * (count - 1) // 2).sum(),
                (count * (count - 1.) * (count - 2)).sum(),
                (count * (count - 1.) * (2 * count + 5)).sum())

    def normtestFinish(z):
        """Common code between all the normality-test functions.

        :param z: z value
        :type z: :py:class:`float`
        :return: tuple of z(float) and prob(int or float or None)
        :rtype: :py:class:`tuple`
        """
        prob = 2 * distributions.norm.sf(np.abs(z))

        if z.ndim == 0:
            z = z[()]

        return z, prob

    if perspective == 'local':
        matchNA = np.logical_and(np.isnan(x), np.isnan(y))
        x = x[np.logical_not(matchNA)]
        y = y[np.logical_not(matchNA)]

    naReplaceX = np.nanmin(x) - 0.1
    naReplaceY = np.nanmin(y) - 0.1
    np.nan_to_num(x, copy=False, nan=naReplaceX)
    np.nan_to_num(y, copy=False, nan=naReplaceY)

    if x.size != y.size:
        raise ValueError("All inputs to `kendalltau` must be of the same "
                         f"size, found x-size {x.size} and y-size {y.size}")
    elif not x.size or not y.size:
        # Return NaN if arrays are empty
        return np.nan, np.nan, np.nan

    size = x.size
    perm = np.argsort(y)  # sort on y and convert y to dense ranks
    x, y = x[perm], y[perm]
    y = np.r_[True, y[1:] != y[:-1]].cumsum(dtype=np.intp)

    # stable sort on x and convert x to dense ranks
    perm = np.argsort(x, kind='mergesort')
    x, y = x[perm], y[perm]
    x = np.r_[True, x[1:] != x[:-1]].cumsum(dtype=np.intp)

    dis = kendall_dis(x, y)  # discordant pairs

    obs = np.r_[True, (x[1:] != x[:-1]) | (y[1:] != y[:-1]), True]
    cnt = np.diff(np.nonzero(obs)[0]).astype('int64', copy=False)

    ntie = (cnt * (cnt - 1) // 2).sum()  # joint ties
    xtie, x0, x1 = countRankTie(x)  # ties in x, stats
    ytie, y0, y1 = countRankTie(y)  # ties in y, stats

    tot = (size * (size - 1)) // 2

    if xtie == tot or ytie == tot:
        return np.nan, np.nan, np.nan
    # Note that tot = con + dis + (xtie - ntie) + (ytie - ntie) + ntie
    #               = con + dis + xtie + ytie - ntie
    conMinusDis = tot - xtie - ytie + ntie - 2 * dis
    tau = conMinusDis / np.sqrt((tot - xtie)*(tot - ytie))
    conPlusDis = tot - xtie - ytie + ntie
    tauMax = conPlusDis / np.sqrt((tot - xtie) * (tot - ytie))

    # Limit range to fix computational errors
    tau = min(1., max(-1., tau))

    # The p-value calculation is the same for all variants since the p-value
    # depends only on conMinusDis.
    if (xtie == 0 and ytie == 0) and (size <= 33 or
                                      min(dis, tot - dis) <= 1):
        method = 'exact'
    else:
        method = 'asymptotic'

    if xtie == 0 and ytie == 0 and method == 'exact':
        pvalue = mstats_basic._kendall_p_exact(size, tot - dis)
    elif method == 'asymptotic':
        # conMinusDis is approx normally distributed with this variance [3]_
        m = size * (size - 1.)
        var = ((m * (2 * size + 5) - x1 - y1) / 18 +
               (2 * xtie * ytie) / m + x0 * y0 / (9 * m * (size - 2)))
        zVal = conMinusDis / np.sqrt(var)
        _, pvalue = normtestFinish(zVal)
    else:
        raise ValueError(f"Unknown method {method} specified.  Use 'auto', "
                         "'exact' or 'asymptotic'.")

    return tau, pvalue, tauMax


def iciktArray(dataArray,
               globalNA=0,
               perspective='global',
               scaleMax=True,
               diagGood=True):
    """Calls iciKT to calculate ICI-Kendall-Tau between every combination of
    columns in the input 2d array, dataArray. Also replaces any instance of the globalNA in the array with np.nan.

    :param dataArray: 2d array with columns of data to analyze
    :type dataArray: :class:`numpy.ndarray`
    :param globalNA: Optional value to replace with np.nan. Default is 0.
    :type globalNA: :py:class:`float` or :class:`None`
    :param perspective: perspective can be 'local' or 'global'. Default is 'global'.  Global includes (NA,NA) pairs in the calculation, while local does not.
    :type perspective: :py:class:`str`
    :param scaleMax: should everything be scaled compared to the maximum correlation?
    :type scaleMax: :py:class:`bool`
    :param diagGood: should the diagonal entries reflect how many entries in the sample were "good"?
    :type diagGood: :py:class:`bool`
    :return: tuple of the output correlations, raw correlations, pvalues, and max tau 2d arrays
    :rtype: :py:class:`tuple`

    Future Parameters:
    featureNA
    sampleNA

    """
    if globalNA is not None:
        dataArray[dataArray == globalNA] = np.nan

    # bool array where the nans are false
    excludeLoc = np.logical_not(np.isnan(dataArray))

    # creating empty output arrays of correct size
    size = dataArray.shape[1]
    corrArray, pvalArray, tauMaxArray = np.zeros([size, size]), np.zeros([size, size]), np.zeros([size, size])

    iPC = it.combinations(range(size), 2)
    pairwiseComparisons = np.ndarray(shape=(2, (size*(size-1))//2))
    count = 0
    for i in iPC:
        pairwiseComparisons[0, count] = i[0]
        pairwiseComparisons[1, count] = i[1]
        count = count + 1

    if not diagGood:
        extraComparisons = np.tile(np.arange(size), 2).reshape(2, -1)
        pairwiseComparisons = np.concatenate((pairwiseComparisons, extraComparisons), axis=1)

    pairwiseComparisons = pairwiseComparisons.astype(int)
    
    # calls iciKT to calculate ICIKendallTau for every combination in product and stores in a list
    with multiprocessing.Pool() as pool:
        tempList = pool.starmap(iciKT, ((dataArray[:, i[0]], dataArray[:, i[1]], perspective) for i in pairwiseComparisons.T))

    # separates+stores the correlation, pvalue, and tauMax data from every combination at the correct
    # location in the output arrays
    for i, (corr, pval, taumax) in zip(pairwiseComparisons.T, tempList):
        corrArray[i[0], i[1]] = corrArray[i[1], i[0]] = corr
        pvalArray[i[0], i[1]] = pvalArray[i[1], i[0]] = pval
        tauMaxArray[i[0], i[1]] = tauMaxArray[i[1], i[0]] = taumax

    if scaleMax:
        maxCor = np.nanmax(tauMaxArray)
        outArray = corrArray / maxCor
    else:
        outArray = corrArray

    if diagGood:
        nGood = np.sum(excludeLoc, axis=0)
        np.fill_diagonal(outArray, nGood / max(nGood))

    return outArray, corrArray, pvalArray, tauMaxArray
