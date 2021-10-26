The icikt Tutorial
====================



Importing icikt package
~~~~~~~~~~~~~~~~~~~~~~~~~

If the `icikt` is installed, it can be imported::

    import icikt




Using icikt in the command-line interface
-------------------------------------------

The iciktArray function can be accessed from the command line interface::

    Either the "icikt" command or "python3 -m icikt" can be used to run the command line interface.

    > icikt.py -h
    
    Usage:
        icikt.py iciktArray <dataFilePath> [--data-format=<format>] [--replace=<globalNA>] [--mode=<perspective>] [--scale=<scaleMax>] [--diag=<diagGood>]
        icikt.py -h | --help

Using a csv file with no global replace values::

    icikt.py iciktArray test.csv --data-format=csv --replace=None

Using a tsv file with no global replace values::

    icikt.py iciktArray test.tsv --data-format=tsv -- replace=None

Using a csv file with 0 as the replace value::

    icikt.py iciktArray test.csv --data-format=csv
    
Using a csv file in local mode with 0 as the replace value::

    icikt.py iciktArray test.csv --mode=local --data-format=csv 