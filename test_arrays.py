from kendalltau import array_analysis
import numpy as np

x = np.array([np.nan, 5, 3, np.nan, np.nan, 2])
y = np.array([4, 1, 17, 8, np.nan, 6])
z = np.array([6, 10, np.nan, 3, 9, 14])
xyz = np.column_stack((x, y, z))
corr, pval = array_analysis(xyz)

corr
pval

large_array = np.genfromtxt('test_data/large_transcript.csv', delimiter = ",")
tmp_array = large_array[..., 0:50]
import time

start_time = time.time()
l_corr, l_pval = array_analysis(tmp_array)
end_time = time.time()

print(end_time - start_time)
