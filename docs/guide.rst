User Guide
==========

Description
-----------
The ``icikt`` package handles missing data before calculating a correlation
between datasets for variables. The missing values are treated as information from a 
left-centered distribution perspective and are included in the calculation of concordant
and discordant pairs used in calculating the correlation value.

Installation
--------------
The ``icikt`` package runs under Python 3.4+. Use pip_ to install.
Starting with Python 3.4, pip_ is included by default.


Install on Linux, Mac OS X
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

   python3 -m pip install icikt


Install on Windows
~~~~~~~~~~~~~~~~~~

.. code:: bash

   py -3 -m pip install icikt


Upgrade on Linux, Mac OS X
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

   python3 -m pip install icikt --upgrade


Upgrade on Windows
~~~~~~~~~~~~~~~~~~

.. code:: bash

   py -3 -m pip install icikt --upgrade



Get the source code
~~~~~~~~~~~~~~~~~~~
 TBD

Dependencies
------------
The ``icikt`` package depends on several Python libraries. The ``pip`` command
will install all dependencies automatically, but if you wish to install them manually,
run the following commands:

   * numpy for creating and modifying ndarrays of data
      * To install numpy run the following:

        .. code:: bash

           python3 -m pip install numpy  # On Linux, Mac OS X
           py -3 -m pip install numpy    # On Windows

   * scipy for performing the kendall-tau calculations
      * To install the scipy Python library run the following:

        .. code:: bash

           python3 -m pip install scipy  # On Linux, Mac OS X
           py -3 -m pip install scipy    # On Windows
           
   * docopt for a command line interface
      * To install the docopt Python library run the following:
    
        .. code:: bash
    
           python3 -m pip install docopt  # On Linux, Mac OS X
           py -3 -m pip install docopt    # On Windows
           



Basic usage
-----------
To use the ``icikt`` package, input a 2d array with n columns each representing
an array of data for a variable. The `iciktArray` will return 4 n x n 2d arrays for output correlations, raw correlations p-values, and maxTaus.
Each element will correspond to the result of a combination of two columns in the input array. `iciktArray` can also
be called from the command-line interface given the file path for the data along with several optional parameters(more in tutorial).




.. _pip: https://pip.pypa.io/
