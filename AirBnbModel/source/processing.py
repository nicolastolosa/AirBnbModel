"""
Module containing the functions used for processing data in source package.
"""

import pandas as pd


def intersect_index(
    df1: pd.DataFrame | pd.Series, df2: pd.DataFrame | pd.Series, dropna: bool = True
) -> pd.Index:
    """
    Return a pandas.Index object containing the intersection of the indexes of
    the objects passed in df1 and df2.

    Parameters
    ----------
    df1, df2:
        Objects (pandas.DataFrame or pandas.Series) to intersect.
    dropna
        if True, null values will be dropped before return

    Examples
    --------
    >>> df1 = pd.Series(data=[1, 2, 3, 4],
    ...                 index = ['foo', 'bar', 'baz', np.nan])
    >>> df2 = pd.Series(data=[5, 6, 7, 8, 9],
    ...                 index = ['foo', 'bar', 'bar', 'qux', np.nan])
    >>> df1
            col
    foo     1
    bar     2
    baz     3
    NaN     4
    >>> df2
            col
    foo     5
    bar     6
    bar     7
    qux     8
    Nan     9

    Get the intersection between the index of df1 and df2 and drop na

    >>> intersect_index(df1, df2, dropna=True)
    Index(['foo', 'bar'], dtype='object')

    """
    _index = df1.index.intersection(df2.index)

    return _index.dropna() if dropna is True else _index
