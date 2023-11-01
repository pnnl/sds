import sds
import pytest
import pandas as pd

from tests import localfile


@pytest.fixture
def matrix():
    return pd.read_csv(localfile("resources/toy-data.csv"))


def test_safematrix(matrix):
    testmatrix = sds.utils.safematrix(matrix)

    # test with pandas
    pd.testing.assert_frame_equal(testmatrix, matrix)
