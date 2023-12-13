# Installation

## Installing with pip

To install the latest stable release from PyPI:

```bash
pip install lfsir
```

This will install LFSIR and all dependencies.

## Installing from GitHub

To install the development version from GitHub:

```bash
pip install git+https://github.com/Iran-Open-Data/LFSIR.git
```

## Using a Virtual Environment

We highly recommend installing LFSIR within a virtual environment to avoid 
conflicts with system packages.

To create a virtual environment:

=== "Windows (cmd)"
    ``` cmd
    python -m venv c:\path\to\virtual\environment
    ```
=== "Linux (bash)"
    ```
    python -m venv /path/to/virtual/environment
    ```

To activate the virtual environment:

=== "Windows (cmd)"
    ``` cmd
    C:\> <venv>\Scripts\activate.bat
    ```
=== "Linux (bash)"
    ```
    $ source <venv>/bin/activate
    ```

For more information go to the [venv documentation](https://docs.python.org/3/library/venv.html)
or the [Real Python tutorial on virtual environments](https://realpython.com/python-virtual-environments-a-primer/).
