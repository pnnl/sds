import sds
import pytest
import os
import pandas as pd

from tests import localfile


@pytest.fixture
def matrix():
    return pd.read_csv(localfile("resources/toy-data.csv"))


@pytest.fixture
def sdsclass(matrix):
    testsds = sds.downselect.SDSWrapper()
    testsds.set_matrix(matrix)
    return testsds


def test_load_pickle_class(sdsclass):
    # Path to file
    path = localfile("resources/toy-sds-class.pkl")

    # Save to file
    sds.save(path, sdsclass)

    # Load
    testsds = sds.io.load_pickle(path)

    # Check instance is correct type
    assert isinstance(testsds, sds.downselect.SDSWrapper)

    # Check n attribute exists
    assert hasattr(testsds, "n")

    # Check matrix attribute is populated
    assert testsds.matrix is not None

    # Clean up
    os.remove(path)


def test_load_pickle_matrix(matrix):
    # Path to file
    path = localfile("resources/toy-dataset.pkl")

    # Save to file
    sds.save(path, matrix)

    # Load
    testmatrix = sds.io.load_pickle(path)

    # Check instance is correct type
    assert isinstance(testmatrix, pd.DataFrame)

    # Clean up
    os.remove(path)


def test_load_csv(matrix):
    # Path to file
    path = localfile("resources/toy-dataset.csv")

    # Save to file
    sds.save(path, matrix)

    # Load
    testmatrix = sds.io.load_csv(path)

    # Check instance is correct type
    assert isinstance(testmatrix, pd.DataFrame)

    # Clean up
    os.remove(path)


def test_load_tsv(matrix):
    # Path to file
    path = localfile("resources/toy-dataset.tsv")

    # Save to file
    sds.save(path, matrix)

    # Load
    testmatrix = sds.io.load_tsv(path)

    # Check instance is correct type
    assert isinstance(testmatrix, pd.DataFrame)

    # Clean up
    os.remove(path)


def test_load_numpy(matrix):
    # Path to file
    path = localfile("resources/toy-dataset.npz")

    # Save to file
    sds.save(path, matrix)

    # Load
    testmatrix = sds.io.load_numpy(path)

    # Check instance is correct type
    assert isinstance(testmatrix, pd.DataFrame)

    # Clean up
    os.remove(path)


@pytest.mark.parametrize(
    "path,instance",
    [
        (localfile("resources/toy-sds-class.pkl"), sds.downselect.SDSWrapper),
    ],
)
def test_load(sdsclass, path, instance):
    # Save
    sds.save(path, sdsclass)

    # Load
    testdata = sds.load(path)

    # Check not none
    assert testdata is not None

    # Check correct type
    assert isinstance(testdata, instance)

    # Clean up
    os.remove(path)


def test_save_csv(matrix):
    # Output path
    path = localfile("resources/toy-dataset.csv")

    # Save to csv
    sds.io.save_csv(path, matrix)

    # Check path exists
    assert os.path.exists(path)

    # Check not empty
    assert os.path.getsize(path) > 0

    # Clean up
    os.remove(path)


def test_save_numpy(matrix):
    # Output path
    path = localfile("resources/toy-dataset.npz")

    # Save to numpy
    sds.io.save_numpy(path, matrix)

    # Check path exists
    assert os.path.exists(path)

    # Check not empty
    assert os.path.getsize(path) > 0

    # Clean up
    os.remove(path)


def test_save_pickle(matrix):
    # Output path
    path = localfile("resources/toy-dataset.pkl")

    # Save to pickle
    sds.io.save_pickle(path, matrix)

    # Check path exists
    assert os.path.exists(path)

    # Check not empty
    assert os.path.getsize(path) > 0

    # Clean up
    os.remove(path)


def test_save_tsv(matrix):
    # Output path
    path = localfile("resources/toy-dataset.tsv")

    # Save to tsv
    sds.io.save_tsv(path, matrix)

    # Check path exists
    assert os.path.exists(path)

    # Check not empty
    assert os.path.getsize(path) > 0

    # Clean up
    os.remove(path)


@pytest.mark.parametrize(
    "path",
    [
        (localfile("resources/toy-sds-class.pkl")),
    ],
)
def test_save(sdsclass, path):
    # Save
    sds.save(path, sdsclass)

    # Check path exists
    assert os.path.exists(path)

    # Check not empty
    assert os.path.getsize(path) > 0

    # Clean up
    os.remove(path)
