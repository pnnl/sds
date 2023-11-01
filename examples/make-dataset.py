'''Generates the toy dataset
'''

import random
import pandas as pd
import numpy as np
random.seed(4) # used 2 for N = 22, used 4 for N = 24


# for 20 items, there are 20 choose 2 = 190 possible pairwise relations. 
# Make an NxN matrix, which is symmetric across the diagonal 

N = 24
mtrx = []

# Build upper right half
for i in range(N):
    row = []
    
    for j in range(i):
        row.append(88)
    row.append(np.nan)
    for k in range(N-1-i):
        row.append(random.random())
    mtrx.append(row)
        
# Reflect across diagonal
df = pd.DataFrame(mtrx)
for i in range(len(df.columns)):
    df[i] = df.loc[i]


df.to_csv(f'toy-{N}x{N}-dataset.csv', index=False)
