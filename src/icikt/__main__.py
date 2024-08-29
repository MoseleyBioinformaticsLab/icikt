"""
Python Information-Content-Informed Kendall Tau Correlation (ICIKT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Usage:
    icikt.py iciktArray <dataFilePath> [--data-format=<format>] [--replace=<globalNA>] [--mode=<perspective>] [--scale=<scaleMax>] [--diag=<diagGood>] [--chunk=<chunkSize>] [--output=<outname>] [--include=<includeOnly>]
    icikt.py leftCensor <dataFilePath> [--data-format=<format>] [--replace=<globalNA>] [--samples=<sampleClasses>]
    icikt.py -h | --help
    icikt.py --version

Options:
    -h, --help                  Shows this screen.
    --version                   Display current version of icikt
    --data-format=<format>      Input file format, available formats: csv, tsv [default: csv].
    --replace=<globalNA>        Values to be replaced with nan, give as a comma separated string [default: nan,inf,0].
    --mode=<perspective>        Options are global or local [default: global].
    --scale=<scaleMax>          Should everything be scaled compared to the maximum correlation [default: True]?
    --diag=<diagGood>           Should the diagonal entries reflect how many entries in the sample were "good" [default: True]?
    --chunk=<chunkSize>         What should the size of the chunks be for multiprocessing [default: 1]?
    --output=<outname>          If you want to save results as a csv, specify the path/to/save/fileID
    --include=<includeOnly>     Only run correlations of specified columns/combinations
    --samples=<sampleClasses>   Which samples are in which classes? Specify a path to a csv.

"""

import icikt
import multiprocessing
import docopt
import numpy as np
import logging as log
import sys


def main():
    args = docopt.docopt(__doc__)

    if args["--version"]:
        print(icikt.__version__)

    if args["leftCensor"]:

        if args["--data-format"] == "tsv":
            args["<dataFilePath>"] = np.genfromtxt(args["<dataFilePath>"], delimiter='\t')
        elif args["--data-format"] == "csv":
            args["<dataFilePath>"] = np.genfromtxt(args["<dataFilePath>"], delimiter=',')
        else:
            log.error(f'"{args["--data-format"]}" is not a valid format. Valid values are "csv" or "tsv".')
            sys.exit(1)

        if args['--replace'] in ('None', ''):
            args["--replace"] = []
        else:
            try:
                args["--replace"] = args["--replace"].split(',')
                args["--replace"] = [float(r) for r in args["--replace"]]
            except ValueError:
                log.error(f"Error. {args['--replace']} is not a valid input. Please give comma separated values that "
                          f"can be cast as float.")
                sys.exit(1)

        if args['--samples'] is not None:
            try:
                args['--samples'] = np.genfromtxt(args['--samples'], delimiter=',')
            except FileNotFoundError:
                log.error(f'"{args["--sample"]}" is not a valid file path.')
                sys.exit(1)

        try:
            results = icikt.leftCensorTest(args["<dataFilePath>"], globalNA=args["--replace"], sampleClasses=args["--samples"])
            print(results)
        except Exception as e:
            print(e)

    if args["iciktArray"]:

        if args["--data-format"] == "tsv":
            args["<dataFilePath>"] = np.genfromtxt(args["<dataFilePath>"], delimiter='\t')
        elif args["--data-format"] == "csv":
            args["<dataFilePath>"] = np.genfromtxt(args["<dataFilePath>"], delimiter=',')
        else:
            log.error(f'"{args["--data-format"]}" is not a valid format. Valid values are "csv" or "tsv".')
            sys.exit(1)

        if args['--replace'] in ('None', ''):
            args["--replace"] = []
        else:
            try:
                args["--replace"] = args["--replace"].split(',')
                args["--replace"] = [float(r) for r in args["--replace"]]
            except ValueError:
                log.error(f"Error. {args['--replace']} is not a valid input. Please give comma separated values that "
                          f"can be cast as float.")
                sys.exit(1)

        if args["--scale"] == "False":
            args["--scale"] = False
        elif args["--scale"] == 'True':
            args["--scale"] = True
        else:
            log.error(f'"{args["--scale"] = }" is not a valid boolean. Valid values are "True" or "False".')
            sys.exit(1)

        if args["--diag"] == "False":
            args["--diag"] = False
        elif args["--diag"] == 'True':
            args["--diag"] = True
        else:
            log.error(f'"{args["--scale"] = }" is not a valid boolean. Valid values are "True" or "False".')
            sys.exit(1)

        if args["--mode"] not in ('local', 'global'):
            log.error(f'"{args["--mode"] = }" is not a valid perspective. Valid values are "local" or "global".')
            sys.exit(1)

        try:
            int(args['--chunk'])
        except ValueError:
            log.error(f"Error: '{args['--chunk'] = }' is not a valid integer.")
            sys.exit(1)

        try:
            out, corr, pVal, tMax = icikt.iciktArray(dataArray=args["<dataFilePath>"], globalNA=args["--replace"], perspective=args["--mode"], scaleMax=args["--scale"], diagGood=args["--diag"], chunkSize=int(args["--chunk"]), includeOnly=args['--include'])

            if args["--output"] is not None:
                np.savetxt(args["--output"]+'outArray.csv', out, delimiter=',')
                np.savetxt(args["--output"]+'corrArray.csv', corr, delimiter=',')
                np.savetxt(args["--output"]+'pValArray.csv', pVal, delimiter=',')
                np.savetxt(args["--output"]+'tMaxArray.csv', tMax, delimiter=',')
            else:
                print(out, corr, pVal, tMax, sep='\n\n')
        except Exception as e:
            print(e)

