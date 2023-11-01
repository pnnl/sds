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
    data
        Pandas dataframe of NxN matrix.

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
    obj : `pandas.DataFrame`
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
    obj : `pandas.DataFrame`
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
    data : object
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
    obj : `pandas.DataFrame`
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
        Path to save file. Supported extensions include .pkl, .mfj, .xyz, .mol,
        .pdb, .inchi, .smi.
    data : obj
        Object instance. Must be :obj:`~isicle.geometry.Geometry` or
        :obj:`~isicle.geometry.XYZGeometry` for .xyz and .mfj.

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
