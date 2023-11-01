import sds
import pytest
import os
import pandas as pd

from tests import localfile


@pytest.fixture
def matrix():
    return pd.read_csv("toy-dataset.csv")


@pytest.fixture
def sdsclass(matrix):
    testsds = sds.downselect.SDS()
    testsds.set_matrix(matrix)
    testsds.check_matrix()
    return testsds


def test_load_pickle(sdsclass):
    # Path to file
    path = localfile("resources/toy-sds-class.pkl")

    # Save to file
    sds.save(path, sdsclass)

    # Load
    testsds = sds.io.load_pickle(path)

    # Check instance is correct type
    assert isinstance(testsds, sds.downselect.SDS)

    # Check xyz attribute exists
    assert hasattr(testsds, "n")

    # Check xyz attribute is populated
    assert sds.matrix is not None

    # Clean up
    os.remove(path)


def test_load_pickle(matrix):
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
