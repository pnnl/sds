import pandas as pd
import numpy as np
import os
import pickle


def load_csv(path):
    """
    Load comma separated file (.csv).

    Parameters
    ----------
    path : str
        Path to csv.

    Returns
    -------
    data
        Pandas dataframe of NxN matrix.

    """
    return pd.read_csv(path)


def load_numpy(path):
    """
    Load numpy file (.npz).

    Parameters
    ----------
    path : str
        Path to .npz.

    Returns
    -------
    data
        Pandas dataframe of NxN matrix.

    """
    npz = np.load(path)
    df = pd.DataFrame.from_dict({item: npz[item] for item in npz.files}, orient="index")
    return df


def load_pickle(path):
    """
    Load pickled file.

    Parameters
    ----------
    path : str
        Path to pickle.

    Returns
    -------
    data
        Pandas dataframe of NxN matrix.

    """
    # Load file
    with open(path, "rb") as f:
        return pd.read_pickle.load(f)


def load_tsv(path):
    """
    Load tab separated file (.tsv).

    Parameters
    ----------
    path : str
        Path to tsv.

    Returns
    -------
    data
        Pandas dataframe of NxN matrix.

    """
    return pd.read_csv(path, sep="\t")


def load(path):
    """
    Load matrix containing file.

    Parameters
    ----------
    path : str
        Path to file containing matrix.

    Returns
    -------
    data
        Pandas dataframe of NxN matrix.

    """
    if (type(path)) == str:
        path = path.strip()
        extension = os.path.splitext(path)[-1].lower()
    if extension == ".pkl":
        return load_pickle(path)
    elif extension == ".npz":
        return load_numpy(path)
    elif extension == ".csv":
        return load_csv(path)
    elif extension == ".tsv":
        return load_tsv(path)


def save_csv(path, obj):
    obj.to_csv(path, index=False)


def save_pickle(path, obj):
    """
    Save object as pickle file.

    Parameters
    ----------
    path : str
        Path to output file.
    data : object
        Aribtrary object instance.

    """

    with open(path, "wb") as f:
        pickle.dump(obj, f)


def save(path, obj):
    if (type(path)) == str:
        path = path.strip()
        extension = os.path.splitext(path)[-1].lower()
    if extension == ".csv":
        return save_csv(path, obj)
    elif extension == ".pkl":
        return save_pickle(path, obj)
