from sds import utils, io
import numpy as np
import pandas as pd
from math import log


class SDSWrapper:
    _defaults = ["n", "matrix"]
    _default_value = [3, None]

    def __init__(self, **kwargs):
        self.__dict__.update(dict(zip(self._defaults, self._default_value)))
        self.__dict__.update(**kwargs)

    def _check_matrix(self, matrix):
        return utils.safematrix(matrix)

    def set_matrix(self, matrix):
        self.matrix = self._check_matrix(matrix)
        self.N = len(self.matrix)

    def _check_n(self, n):
        """
        Check and reduce n to maximum number of dimension.
        """
        M = len(self.matrix.dropna(how="all"))
        if n > M:
            n = M
        return n

    def set_n(self, n: int):
        if self.matrix is None:
            raise ("Matrix must be set prior to n.")
        self.n = self._check_n(n)

    def search(self):
        if self.matrix is None:
            raise ("Matrix must be set prior to search.")
        # First grab matrix indices of the two most dissimilar geometries
        row_mx = []

        for i in range(self.N):
            row_mx.append(np.nanmax(self.matrix.loc[i]))
        ind1 = np.nanargmax(row_mx)
        ind2 = ind1 + 1 + np.nanargmax(row_mx[ind1 + 1 :])

        # Initialize the dissimilar matrix with the two most dissimilar
        disarray = [np.array(self.matrix.loc[ind1]), np.array(self.matrix.loc[ind2])]
        indices = [ind1, ind2]

        # Find n-2 other most dissimilar
        # Multiply the rows of the n-1 dissimilar set. Or,
        # use log summing if N is large (e.g. 50000) to avoid
        # exceeding floating point machine precision.
        # This script uses log summing.
        # The index of the largest value is the index of the nth
        # item which makes the nth dissimilar set.

        # Initialize array for log summing
        logsum = [0 for x in range(self.N)]
        logsum += np.log(disarray[0])

        for i in range(self.n - 2):
            logsum += np.log(disarray[-1])
            indn = np.nanargmax(logsum)
            indices.append(indn)
            disarray.append(np.array(self.matrix.loc[indn]))

        self.res = pd.DataFrame([indices], index=["matrix index"]).T

    def post_process(self):
        narray = np.array([x for x in range(1, self.n + 1)])
        res = self.res
        res["n Dissimilar"] = narray
        self.res = res

    def benchmark(self):
        idx = self.res["matrix index"].values
        self.matrix.columns = self.matrix.columns.astype(int)
        submatrix = self.matrix[idx].loc[idx]
        submatrix = submatrix.applymap(log)
        final_sum = submatrix.sum().sum() / 2
        self.final_sum = final_sum

    def save(self, path="SDS_N{self.N}_{self.n}_dissimilar.csv"):
        io.save_csv(path, self.res)

    def run(self, matrix, n):
        self.set_matrix(matrix)
        self.set_n(n)
        self.search()
        self.post_process()
        return self
