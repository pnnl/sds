'''Find the exact solution of the toy dataset
'''
from itertools import combinations
import numpy as np
import pandas as pd
from time import time

START = time()

N = 24 # Population size
n = 12 # dissimilar-set size


# Load dataset, reset column labels while doing so because pandas will interpret as string
mtrx = pd.read_csv(f'toy-{N}x{N}-dataset.csv', skiprows=1, header=None)

# Run through all possible combinations
sums = []
for subset in combinations(mtrx.index, n):
   submtrx = mtrx[list(subset)].loc[list(subset)]
   sums.append(submtrx.sum().sum()/2)
   

sums = np.array(sums)
df = pd.DataFrame([sums.max(), sums.mean(), sums.min()], index=['max set', 'mean set', 'min set']).T
df.to_csv(f'exact-solution-N{N}-n{n}.csv', index=False)

print(f'Exact solution N = {N}, n = {n}')
print((time()-START)/60, ' min')

