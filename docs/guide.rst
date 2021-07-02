User Guide
==========

Description
-----------
The :mod:`pythonICIKendallTau` package handles missing data before calculating a correlation
between datasets for variables.

Installation
--------------
The ``pyICIKendallTau`` package runs under Python 3.4+. Use pip_ to install.
Starting with Python 3.4, pip_ is included by default.


Install on Linux, Mac OS X
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

   python3 -m pip install pyicikt


Install on Windows
~~~~~~~~~~~~~~~~~~

.. code:: bash

   py -3 -m pip install pyicikt


Upgrade on Linux, Mac OS X
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

   python3 -m pip install pyicikt --upgrade


Upgrade on Windows
~~~~~~~~~~~~~~~~~~

.. code:: bash

   py -3 -m pip install pyicikt --upgrade



Get the source code
~~~~~~~~~~~~~~~~~~~
 TBD

Dependencies
------------
The :mod:`pythonICIKendallTau` package depends on several Python libraries. The ``pip`` command
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



Basic usage
-----------
The :mod:`pythonICIKendallTau` package can be used in two ways:
     * Calculating correlation between  2 variables
         * Inputing 2 1d arrays for each variable into the iciKT function will return 
           a short list containing the correlation value and p-value.
     * Calculating correlations between n variables
         *