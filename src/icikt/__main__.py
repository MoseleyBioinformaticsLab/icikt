"""
Python Information-Content-Informed Kendall Tau Correlation (ICIKT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Usage:
    icikt.py iciktArray <dataFilePath> [--data-format=<format>] [--replace=<globalNA>] [--mode=<perspective>] [--scale=<scaleMax>] [--diag=<diagGood>] [--output=<outname>]
    icikt.py -h | --help
    icikt.py --version

Options:
    -h, --help                  Shows this screen.
    --version                   Display current version of icikt
    --data-format=<format>      Input file format, available formats: csv, tsv [default: csv].
    --replace=<globalNA>        Value to be replaced with nan [default: 0].
    --mode=<perspective>        Options are global or local [default: global].
    --scale=<scaleMax>          Should everything be scaled compared to the maximum correlation [default: TRUE]?
    --diag=<diagGood>           Should the diagonal entries reflect how many entries in the sample were "good" [default:TRUE]?
    --output=<outname>          If you want to save results as a csv, specify the path/to/save/fileID

"""

from . import iciktArray
from . import __version__ as ver
import docopt
import numpy as np


def main():
    args = docopt.docopt(__doc__)
    if args["--version"]:
        print(ver)
    if args["iciktArray"]:

        if args["--data-format"] == "tsv":
            args["<dataFilePath>"] = np.genfromtxt(args["<dataFilePath>"], delimiter='\t')
        else:
            args["<dataFilePath>"] = np.genfromtxt(args["<dataFilePath>"], delimiter=',')

        if args["--replace"] == 'None':
            args["--replace"] = None
        if args["--replace"] is not None:
            args["--replace"] = float(args["--replace"])

        out, corr, pVal, tMax = iciktArray(args["<dataFilePath>"], args["--replace"], args["--mode"], args["--scale"], args["--diag"])
        if args["--output"] is not None:
            np.savetxt(args["--output"]+'outArray.csv', out, delimiter=',')
            np.savetxt(args["--output"]+'corrArray.csv', corr, delimiter=',')
            np.savetxt(args["--output"]+'pValArray.csv', pVal, delimiter=',')
            np.savetxt(args["--output"]+'tMaxArray.csv', tMax, delimiter=',')
        else:
            print(out, corr, pVal, tMax, sep='\n\n')




if __name__ == "__main__":
    main()
