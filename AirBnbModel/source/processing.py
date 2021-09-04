"""
Module containing the functions used for processing data in source package.
"""

import pandas as pd


def intersect_index(input1, input2, dropna: bool = True) -> pd.Index:
    """
    Return a pandas.Index object containing the intersection of the indexes of
    the objects passed in input1 and input2.

    Parameters
    ----------
    input1, input2 : pandas.DataFrame or pandas.Series
        Objects (pandas.DataFrame or pandas.Series) to intersect.
    dropna
        if True, null values will be dropped before return

    Examples
    --------
    >>> input1 = pd.Series(data=[1, 2, 3, 4],
    ...                 index = ['foo', 'bar', 'baz', np.nan])
    >>> input2 = pd.Series(data=[5, 6, 7, 8, 9],
    ...                 index = ['foo', 'bar', 'bar', 'qux', np.nan])
    >>> input1
            col
    foo     1
    bar     2
    baz     3
    NaN     4
    >>> input2
            col
    foo     5
    bar     6
    bar     7
    qux     8
    Nan     9

    Get the intersection between the index of input1 and dfinput22 and drop na

    >>> intersect_index(input1, input2, dropna=True)
    Index(['foo', 'bar'], dtype='object')

    """
    assert isinstance(input1, pd.DataFrame) or isinstance(
        input1, pd.Series
    ), "input1 is not either a pandas DataFrame or Series"
    assert isinstance(input2, pd.DataFrame) or isinstance(
        input2, pd.Series
    ), "input2 is not either a pandas DataFrame or Series"

    _index = input1.index.intersection(input2.index)

    return _index.dropna() if dropna is True else _index
