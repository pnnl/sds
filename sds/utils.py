import numpy as np
import pandas as pd


def safematrix(x):
    """
    Ensures passed object is of correct format.

    Parameters
    ----------
    x : any
        Object to be cast as matrix.
    Returns
    -------
    list, :obj:`~pd.core.series.Series`, or :obj:`~np.ndarray`
        Input safely cast to list-like.

    """

    if not isinstance(x, (pd.DataFrame, np.ndarray)):
        raise ValueError(
            "matrix object is not a valid Pandas DataFrame or Numpy ndarray"
        )
    if isinstance(x, pd.DataFrame):
        N = len(x.index)
        assert N == len(x.columns)
    if isinstance(x, np.ndarray):
        # TODO check dimensionality of numpy array
        pass
    return x.copy()
