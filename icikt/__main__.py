"""
Python Information-Content-Informed Kendall Tau Correlation (ICIKT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Usage:
    icikt.py iciktArray <dataFilePath> [--mode=<type>] [--data-format=<format>] [--replace=<globalNA>]
    icikt.py -h | --help

Options:
    -h, --help                      Shows this screen.
    --mode=<type>                 Options are global or local [default: global].
    --data-format=<format>          Input file format, available formats: csv, tsv [default: csv].
    --replace=<globalNA>        Value to be replaced with nan.
"""

from . import icikt
import docopt
import numpy as np


def main():
    args = docopt.docopt(__doc__)
    if args["iciktArray"]:

        if args["--data-format"] == "tsv":
            args["<dataFilePath>"] = np.genfromtxt(args["<dataFilePath>"], delimiter='\t')
        else:
            args["<dataFilePath>"] = np.genfromtxt(args["<dataFilePath>"], delimiter=',')

        if args["--replace"] == 'None':
            args["--replace"] = None
        if args["--replace"] is not None:
            args["--replace"] = float(args["--replace"])

        icikt.iciktArray(args["<dataFilePath>"], args["--replace"], args["--mode"])


if __name__ == "__main__":
    main()
