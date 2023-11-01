from sds import utils, io
import numpy as np
import pandas as pd
from math import log


def SDS(matrix, n):
    return SDSWrapper().run(matrix, n)


class SDSWrapper:
    """
    Wrapper for Similarity Down Selection functionality.

    Finds the `n` most dissimilar items. In the input matrix, the ith row (and
    ith column) is an array belonging to item i. The matrix element (i,j) would
    then be the pairwise dissimilarity metric between items i and j (e.g.,
    geometric RMSD between molecular conformers i and j).


    Attributes
    ----------
    n : int
        Set size of most dissilimar elements to return from population.
        1 < n < N, where N is the full population size.

    matrix : :obj:`~pd.DataFrame`
        Pandas DataFrame of NxN dimension containing matrix.

        Square matrix where each row (and by symmetry, column) is an array
        corresponding to a specific item or object, and each element (i,j) the
        floating point dissimilarity between items i and j. The element (i,i)
        must be represented as np.nan (for log-summing).

        If pairwise data between two items is missing, this can also be
        represented as np.nan. Second item will automatically be set to np.nan
        in the log-summation array once the first of one of the two items is
        chosen. Thus, the second item will never be chosen. In this same
        manner, entire missing items can be represented as arrays of np.nan,
        as a trick to preserve externally related indexing.
    N : int
        Dimension of matrix object and full population size.
    res : :obj:`~pd.DataFrame`
        Resultant Pandas DataFrame of indices for n most dissimilar elements.
        Ordering is ranked from 1st most dissimilar.
    final_sum : float
        Summed dissimilarity
    """

    _defaults = ["n", "matrix"]
    _default_value = [3, None]

    def __init__(self, **kwargs):
        """
        Initialize :obj:`~sds.downselect.SDSWrapper` instance.
        """
        self.__dict__.update(dict(zip(self._defaults, self._default_value)))
        self.__dict__.update(**kwargs)

    def _check_matrix(self, matrix):
        """
        Check matrix is :obj:`pd.DataFrame` and of NxX dimension.
        """
        return utils.safematrix(matrix)

    def set_matrix(self, matrix):
        """
        Set matrix and dimension attributes.
        """
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
        """
        Set n attribute, or returned set size.
        """
        if self.matrix is None:
            raise ("Matrix must be set prior to n.")
        self.n = self._check_n(n)

    def search(self):
        """
        Execute similarity down selection algorithm.

        """
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
        """
        Add ranking numbers to ordered rank from search.
        """
        narray = np.array([x for x in range(1, self.n + 1)])
        res = self.res
        res["n Dissimilar"] = narray
        self.res = res

    def benchmark(self):
        """
        Calculate summed dissimilarity.
        """
        idx = self.res["matrix index"].values
        self.matrix.columns = self.matrix.columns.astype(int)
        submatrix = self.matrix[idx].loc[idx]
        submatrix = submatrix.applymap(log)
        final_sum = submatrix.sum().sum() / 2
        self.final_sum = final_sum

    def save(self, path, obj):
        """
        Save provided object (e.g., self.res or self) to path.
        """
        io.save(path, obj)

    def run(self, matrix, n):
        """
        Helper function to streamline execution of key functions.
        """
        self.set_matrix(matrix)
        self.set_n(n)
        self.search()
        self.post_process()
        self.benchmark()
        return self
