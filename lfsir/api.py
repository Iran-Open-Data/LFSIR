"""LFSIR, Labor Force Survey of Iran, Main API
"""
# pylint: disable=too-many-arguments
# pylint: disable=unused-argument
# pylint: disable=too-many-locals

from pathlib import Path
from typing import Literal

import pandas as pd

from bssir.metadata_reader import config, _Years
from bssir.api import API

defaults, metadata = config.set_package_config(Path(__file__).parent)
api = API(defaults=defaults, metadata=metadata)

_Table = Literal["data"]


def __get_optional_params(local_variables: dict) -> dict:
    return {key: value for key, value in local_variables.items() if value is not None}


def load_table(
    table_name: _Table = "data",
    years: _Years = "last",
    form: Literal["normalized", "cleaned", "raw"] | None = None,
    *,
    on_missing: Literal["error", "download", "create"] | None = None,
    redownload: bool | None = None,
    save_downloaded: bool | None = None,
    recreate: bool | None = None,
    save_created: bool | None = None,
) -> pd.DataFrame:
    """Load a table for the given table name and year(s).

    This function loads original survey tables as well as package
    tables defined in this library.

    Original survey tables are available in three forms:

    - 'raw' - Contains the raw survey data without any modifications
    - 'cleaned' - Raw data with added labels, types, removed irrelevant
        values, but no changes to actual data
    - 'normalized' - Standardized data form with consistent column
        names, value encodings and table structure applied across data
        from multiple survey years. Also adds useful metadata like
        table name and year identifiers.

    Package tables are defined in this library to facilitate working
    with the data and are only available in normalized form.

    For more details on available tables, see the documentation
    [tables page](https://iran-open-data.github.io/LFSIR/tables/).

    !!! note
        The `years` parameter accepts different input types:

        - int: A single year integer like 1390 or 90
        - list[int]: A list of integer years [1390, 1395, 1400]
        - str: A hyphenated string range like '1390-1395'
        - "all": A string indicating all available years
        - "last": A string indicating only the most recent year

    Parameters
    ----------
    table_name : _Table, default "data"
        The name of the table to load.
    years : _Years, default "last"
        The years of data to load.
    form : {"normalized", "cleaned", "raw"}, default "normalized"
        The form of the data to load. Options are "normalized",
        "cleaned", or "raw".

    Other parameters
    ----------------
    on_missing : {"download", "create", "error"}, default "download"
        Behavior if table is missing. "download" downloads the table,
        "create" generates table from raw data, "error" raises an
        exception.
    redownload : bool, default False
        Whether to re-download table if it exists.
    save_downloaded : bool, default True
        Whether to save newly downloaded data.
    recreate : bool, default False
        Whether to recreate table if it exists.
    save_created : bool, default True
        Whether to save newly created data.

    Returns
    -------
    pd.DataFrame
        Loaded table as a pandas DataFrame.

    Raises
    ------
    FileNotFoundError
        If data is missing and on_missing='error'.


    Examples
    --------
        >>> import lfsir
        >>> df = lfsir.load_table("data", 1400) # Loads survey data for year 1400
        >>> df.iloc[:5, :5]
               ID  Census_Turn  Alternative_Household  Survey_Taken Survey_Skip_Reason
        0  100141            4                  False          True               None
        1  100141            4                  False          True               None
        2  100142            3                  False          True               None
        3  100142            3                  False          True               None
        4  100142            3                  False          True               None

    """

    parameters = __get_optional_params(locals())
    return api.load_table(**parameters)
