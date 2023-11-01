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
    data, :obj:`~pd.DataFrame`
        Input safely cast to Pandas DataFrame.

    """

    if not isinstance(x, (pd.DataFrame)):
        raise ValueError("Matrix object is not a valid Pandas DataFrame")
    if isinstance(x, pd.DataFrame):
        N = len(x.index)
        assert N == len(x.columns)
    return x.copy()
