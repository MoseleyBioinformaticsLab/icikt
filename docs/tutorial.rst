The icikt Tutorial
====================



Importing icikt package
~~~~~~~~~~~~~~~~~~~~~~~~~

If the ``icikt`` package is installed, it can be imported::

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

    icikt.py iciktArray test.tsv --data-format=tsv --replace=None

Using a csv file with 0 as the replace value::

    icikt.py iciktArray test.csv --data-format=csv
    
Using a csv file in local mode with 0 as the replace value::

    icikt.py iciktArray test.csv --mode=local --data-format=csv


Using icikt in a Python script
--------------------------------
Import numpy and icikt:

.. code:: python

        import numpy as np
        import icikt

Generate a numpy array from your data file:

.. code:: python

        dataArray = np.genfromtxt('path/to/file.tsv', delimiter='\t')

Call iciktArray on your dataArray, saving outputs to separate variables:

.. code:: python

        out, corr, pVal, tMax = icikt.iciktArray(dataArray)
        print(out,corr,pVal,tMax,sep='\n\n')
        
        # saving outputs to files
        np.savetxt('outArray.csv', out, delimiter=',')
        np.savetxt('corrArray.csv', corr, delimiter=',')
        np.savetxt('pValArray.csv', pVal, delimiter=',')
        np.savetxt('tMaxArray.csv', tMax, delimiter=',')
