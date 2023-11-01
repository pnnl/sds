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
    data, :obj:`~pd.DataFrame`
        Pandas DataFrame of NxN matrix.

    """
    return pd.read_csv(path)


def load_numpy(path, key="arr_0"):
    """
    Load numpy file (.npz).

    Parameters
    ----------
    path : str
        Path to .npz.
    key : str
        Accession key of .npz, default is arr_0.

    Returns
    -------
    data, :obj:`~pd.DataFrame`
        Pandas DataFrame of NxN matrix.

    """
    npz = np.load(path)[key]
    df = pd.DataFrame.from_dict(
        {elem: item for elem, item in enumerate(npz)}, orient="index"
    )
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
    data, :obj:`~pd.DataFrame`
        Pandas DataFrame of NxN matrix.

    """
    # Load file
    with open(path, "rb") as f:
        return pd.read_pickle(f)


def load_tsv(path):
    """
    Load tab separated file (.tsv).

    Parameters
    ----------
    path : str
        Path to tsv.

    Returns
    -------
    data, :obj:`~pd.DataFrame`
        Pandas DataFrame of NxN matrix.

    """
    return pd.read_csv(path, sep="\t")


def load(path):
    """
    Load object, format detected by path extension.

    Parameters
    ----------
    path : str
        Path to file containing object. Supported extensions include .pkl, .csv, .tsv, .npz

    Returns
    -------
    data, :obj:`~pd.DataFrame`
        Data object (e.g., Pandas DataFrame of SDS class).

    """
    if (type(path)) == str:
        path = path.strip()
        extension = os.path.splitext(path)[-1].lower()
    if extension == ".pkl":
        return load_pickle(path)
    if extension == ".npz":
        return load_numpy(path)
    if extension == ".csv":
        return load_csv(path)
    if extension == ".tsv":
        return load_tsv(path)
    raise IOError("Extension {} not recognized.".format(extension))


def save_csv(path, obj):
    """
    Save Pandas DataFrame as comma separated file.

    Parameters
    ----------
    path : str
        Path to output file.
    obj, :obj:`~pd.DataFrame`
        Matrix object as Pandas DataFrame.
    """
    if not isinstance(obj, pd.DataFrame):
        raise ValueError("object is not a valid Pandas DataFrame")
    obj.to_csv(path, index=False)


def save_numpy(path, obj):
    """
    Save Pandas DataFrame as compressed numpy.

    Parameters
    ----------
    path : str
        Path to output file.
    obj, :obj:`~pd.DataFrame`
        Matrix object as Pandas DataFrame.
    """
    if not isinstance(obj, pd.DataFrame):
        raise ValueError("object is not a valid Pandas DataFrame")
    np.savez(path, obj.to_numpy())


def save_pickle(path, obj):
    """
    Save object as pickle file.

    Parameters
    ----------
    path : str
        Path to output file.
    obj, :obj:`~pd.DataFrame` or `~sds.downselect.SDS`
        Aribtrary object instance.

    """

    with open(path, "wb") as f:
        pickle.dump(obj, f)


def save_tsv(path, obj):
    """
    Save Pandas DataFrame as tab separated file.

    Parameters
    ----------
    path : str
        Path to output file.
    obj, :obj:`~pd.DataFrame`
        Matrix object as Pandas DataFrame.
    """
    if not isinstance(obj, pd.DataFrame):
        raise ValueError("object is not a valid Pandas DataFrame")
    obj.to_csv(path, index=False, sep="\t")


def save(path, obj):
    """
    Save object, format detected by path extension.

    Parameters
    ----------
    path : str
        Path to save file. Supported extensions include .pkl, .csv, .tsv, .npz
    obj, :obj:`~pd.DataFrame` or `~sds.downselect.SDS`
        Arbitrary object instance.
    """
    if (type(path)) == str:
        path = path.strip()
        extension = os.path.splitext(path)[-1].lower()
    if extension == ".csv":
        return save_csv(path, obj)
    if extension == ".tsv":
        return save_tsv(path, obj)
    if extension == ".npz":
        return save_numpy(path, obj)
    if extension == ".pkl":
        return save_pickle(path, obj)
    raise IOError("Extension {} not recognized.".format(extension))
