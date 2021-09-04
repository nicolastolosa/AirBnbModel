"Test suite of AirBnbModel.source.processing module"

import numpy as np
import pandas as pd
import pytest
from pandas._testing import assert_index_equal

from AirBnbModel.source.processing import intersect_index


class TestIntersectIndex(object):
    "Test suite for intersect_index method"

    def test_first_input_not_pandas_dataframe_or_series(self):
        "First input passed as a list. Should return AssertionError"

        input1 = [1, 2, 3, 4]
        input2 = pd.Series(data=[5, 6, 7, 8], index=["foo", "bar", "bar", "qux"])

        with pytest.raises(AssertionError) as e:
            intersect_index(input1, input2)

        assert e.match("input1 is not either a pandas DataFrame or Series")

    def test_second_input_not_pandas_dataframe_or_series(self):
        "Second input passed as a list. Should return AssertionError"

        input1 = pd.Series(data=[5, 6, 7, 8], index=["foo", "bar", "bar", "qux"])
        input2 = [1, 2, 3, 4]

        with pytest.raises(AssertionError) as e:
            intersect_index(input1, input2)

        assert e.match("input2 is not either a pandas DataFrame or Series")

    def test_index_as_string(self):
        "Index of both inputs are string (object) dtypes."

        input1 = pd.Series(data=[1, 2, 3], index=["foo", "bar", "bar"])
        input2 = pd.Series(data=[4, 5, 6], index=["bar", "foo", "qux"])

        expected = pd.Index(["foo", "bar"])
        actual = intersect_index(input1, input2)

        assert_index_equal(actual, expected), f"{expected} expected. Got {actual}"

    def test_index_as_number(self):
        "Index of both inputs are int dtypes."

        input1 = pd.Series(data=[1, 2, 3], index=[1, 2, 3])
        input2 = pd.Series(data=[4, 5, 6], index=[1, 1, 4])

        expected = pd.Index([1])
        actual = intersect_index(input1, input2)

        assert_index_equal(actual, expected), f"{expected} expected. Got {actual}"

    def test_null_intersection_between_inputs(self):
        "There is not intersection between. Should return an empty pd.Index()"

        input1 = pd.Series(data=[1, 2, 3], index=[1, 2, 3])
        input2 = pd.Series(data=[4, 5, 6], index=[4, 5, 6])

        expected = pd.Index([], dtype="int64")
        actual = intersect_index(input1, input2)

        assert_index_equal(actual, expected), f"{expected} expected. Got {actual}"

    def test_dropna_true(self):
        "Intersection contains NaN values. dropna=True should remove it"

        input1 = pd.Series(data=[1, 2, 3, 4], index=["foo", "bar", "bar", np.nan])
        input2 = pd.Series(data=[5, 6, 7, 8], index=["bar", "foo", "qux", np.nan])

        expected = pd.Index(["foo", "bar"])
        actual = intersect_index(input1, input2, dropna=True)

        assert_index_equal(actual, expected), f"{expected} expected. Got {actual}"

    def test_dropna_false(self):
        "Intersection contains NaN values. dropna=True should not remove it"

        input1 = pd.Series(data=[1, 2, 3, 4], index=["foo", "bar", "bar", np.nan])
        input2 = pd.Series(data=[5, 6, 7, 8], index=["bar", "foo", "qux", np.nan])

        expected = pd.Index(["foo", "bar", np.nan])
        actual = intersect_index(input1, input2, dropna=False)

        assert_index_equal(actual, expected), f"{expected} expected. Got {actual}"
