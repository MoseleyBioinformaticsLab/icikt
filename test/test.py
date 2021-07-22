import numpy as np
import icikt
import time


def smallTest():

    x = np.array([np.nan, 5, 3, np.nan, np.nan, 2])
    y = np.array([4, 0, 17, 8, np.nan, 6])
    z = np.array([6, 10, np.nan, 3, 9, 14])
    xyz = np.column_stack((x, y, z))

    sTime = time.time()
    corr, pval = iciktArray(xyz, replaceVal=0)
    fTime = time.time()

    print(corr)
    print(pval)
    print(fTime - sTime)


def bigTest():

    largeArray = np.genfromtxt('/mlab/data/psbhatt/projects/pythonICIKendallTau/test/bigTest.csv', delimiter=",")

    sTime = time.time()
    corr, pval = iciktArray(largeArray)
    fTime = time.time()

    print(corr)
    print(pval)
    print(fTime - sTime)

