import sds
import pytest
import pandas as pd
from sds.downselect import SDSWrapper

from tests import localfile


@pytest.fixture
def matrix():
    return pd.read_csv(localfile("resources/toy-data.csv"))


@pytest.fixture()
def SDS():
    return SDSWrapper()


class TestSDSWrapper:
    def test_init(self, SDS):
        # Check class initialization
        assert isinstance(SDS, SDSWrapper)

        # Check default
        assert SDS.n == 3

        # Check default
        assert SDS.matrix is None

    def test_set_matrix(self, SDS, matrix):
        # Set matrix
        SDS.set_matrix(matrix)

        # Check matrix attribute exists
        assert hasattr(SDS, "matrix")

        # Check matrix attribute is populated
        assert SDS.matrix is not None

        # Check dimension vairable, N
        assert SDS.N == len(matrix)

    @pytest.mark.parametrize("x,expected", [(3, 3), (2, 2), (21, 20)])
    def test_set_n(self, SDS, matrix, x, expected):
        # Set matrix
        SDS.set_matrix(matrix)

        # Toy-data has dimensions of 20
        SDS.set_n(x)
        assert SDS.n == expected

    def test_search(self, SDS, matrix):
        # Set matrix
        SDS.set_matrix(matrix)

        # Run search algorithm
        SDS.search()

        assert isinstance(SDS.res, pd.DataFrame)

    def test_post_process(self, SDS, matrix):
        # Set matrix
        SDS.set_matrix(matrix)

        # Run search algorithm
        SDS.search()

        # Execute post process
        SDS.post_process()

        assert isinstance(SDS.res, pd.DataFrame)

    def test_benchmark(self, SDS, matrix):
        # Set matrix
        SDS.set_matrix(matrix)

        # Run search algorithm
        SDS.search()

        # Execute post process
        SDS.post_process()

        # Execute benchmark
        SDS.benchmark()

        assert isinstance(SDS.final_sum, float)

    @pytest.mark.parametrize("x,expected", [(3, 3), (2, 2), (21, 20)])
    def test_run(self, SDS, matrix, x, expected):
        # Execute run function
        SDS.run(matrix, x)

        # Check matrix attribute exists
        assert hasattr(SDS, "matrix")

        # Check matrix attribute is populated
        assert SDS.matrix is not None

        # Check dimension vairable, N
        assert SDS.N == len(matrix)

        # Check n attribute
        assert SDS.n == expected
