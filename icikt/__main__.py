"""
Python Information-Content-Informed Kendall Tau Correlation (ICIKT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Usage:
    icikt.py iciktArray <dataFilePath> [--data-format=<format>] [--replace=<globalNA>] [--mode=<perspective>] [--scale=<scaleMax>] [--diag=<diagGood>]
    icikt.py -h | --help

Options:
    -h, --help                      Shows this screen.
    --data-format=<format>      Input file format, available formats: csv, tsv [default: csv].
    --replace=<globalNA>        Value to be replaced with nan [default: 0].
    --mode=<perspective>        Options are global or local [default: global].
    --scale=<scaleMax>          Should everything be scaled compared to the maximum correlation [default: TRUE]?
    --diag=<diagGood>           Should the diagonal entries reflect how many entries in the sample were "good" [default:TRUE]?

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

        icikt.iciktArray(args["<dataFilePath>"], args["--replace"], args["--mode"], args["--scale"], args["--diag"])


if __name__ == "__main__":
    main()
