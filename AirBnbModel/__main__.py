"""
Calls the main function on run.py, which is the single entry point to all
functionality of the package.

This file allows the package to be executed using the standard way from the
command line

>>> python -m AirBnbModel (+ arguments)
"""

from AirBnbModel.run import main_cli

if __name__ == "__main__":
    main_cli()
