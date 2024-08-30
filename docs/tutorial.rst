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

    > icikt -h
    
    Usage:
        icikt.py iciktArray <dataFilePath> [--data-format=<format>] [--replace=<globalNA>] [--mode=<perspective>] [--scale=<scaleMax>] [--diag=<diagGood>] [--chunk=<chunkSize>] [--output=<outname>] [--include=<includeOnly>]
        icikt.py leftCensor <dataFilePath> [--data-format=<format>] [--replace=<globalNA>] [--samples=<sampleClasses>]
        icikt.py -h | --help
        icikt.py --version

Using a csv file with no global replace values::

    icikt iciktArray /path/to/file.csv --data-format=csv --replace=None

Using a tsv file with no replacements and outputting the results with prefix of 'test'::

    icikt iciktArray /path/to/file.tsv --data-format=tsv --replace= --output=test
    
Using a csv file in local mode with 0 as the replace value, no scaling, no diagonal values, and a chunk size of 5::

    icikt iciktArray /path/to/file.csv --replace=0 --mode=local --scale=False --diag=False --chunk=5


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
