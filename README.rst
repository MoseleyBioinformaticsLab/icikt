icikt
=====

Description
--------------
The ``icikt`` package handles missing data before calculating a correlation
between datasets for variables. The missing values are treated as information from a 
left-centered distribution perspective and are included in the calculation of concordant
and discordant pairs used in calculating the correlation value.

Full API documentation, user guide, and tutorial can be found on Github_Pages_

Installation
--------------
The ``icikt`` package runs under Python 3.8+. Use pip_ to install.
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
Code is available on GitHub: https://github.com/MoseleyBioinformaticsLab/icikt

To clone the repo, first make sure you have git_ installed:

.. code:: bash

   git clone https://github.com/MoseleyBioinformaticsLab/icikt.git


Dependencies
~~~~~~~~~~~~
The ``icikt`` package depends on several Python libraries:
    * docopt_ for a command line interface.
    * scipy_ and numpy_ for mathmatical calculations.
    * Cython_ for optimized performance.

NOTE- NumPy and Cython must be preinstalled in order for this package to work.

The ``pip`` command will install all dependencies automatically, but if you wish to install them manually, run the following commands:
   
   * docopt for a command line interface
      * To install the docopt Python library run the following:
    
        .. code:: bash
    
           python3 -m pip install docopt  # On Linux, Mac OS X
           py -3 -m pip install docopt    # On Windows
   
   * scipy for performing the kendall-tau calculations
      * To install the scipy Python library run the following:

        .. code:: bash

           python3 -m pip install scipy  # On Linux, Mac OS X
           py -3 -m pip install scipy    # On Windows

   * numpy for creating and modifying ndarrays of data
      * To install numpy run the following:

        .. code:: bash

           python3 -m pip install numpy  # On Linux, Mac OS X
           py -3 -m pip install numpy    # On Windows

   * Cython for the cythonized kendall_dis method
      * To install the Cython Python library run the following:
    
        .. code:: bash
    
           python3 -m pip install Cython  # On Linux, Mac OS X
           py -3 -m pip install Cython    # On Windows


WARNING- If the following pip error message is generated, then the python3 devel package must be installed:

   .. code:: bash

      "fatal error: Python.h: No such file or directory"


Basic usage
-----------

To use the ``icikt`` package, input a 2d array with n columns each representing
an array of data for a variable. The `iciktArray` will return two n x n 2d arrays for correlations and p-values.
Each element will correspond to the result of a combination of two columns in the input array. iciktArray can also
be called from the command-line interface given the file path for the data along with several optional parameters(more in docs/tutorial).

Running through command line :

.. code:: bash

        icikt iciktArray /path/to/file.tsv --data-format=tsv --replace=None

Running through python script :

.. code:: python

        import numpy as np
        import icikt

        dataArray = np.genfromtxt('/path/to/file.tsv', delimiter="\t")
        # or with random values
        dataArray = np.random.randn(100, 2)

        # running just 2 arrays with icikt
        corr, pVal, tMax = icikt.icikt(dataArray[:,0], dataArray[:,1])
        
        # running all combinations with iciktArray
        scaled, corrRaw, pVals, tauMax = icikt.iciktArray(dataArray)

        


License
-------

A modified Clear BSD License


Copyright (c) 2021, Praneeth S. Bhatt, Robert M. Flight, Hunter N.B. Moseley
All rights reserved.


Redistribution and use in source and binary forms, with or without
modification, are permitted (subject to the limitations in the disclaimer
below) provided that the following conditions are met:


* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.
  
* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
  
* Neither the name of the copyright holder nor the names of its contributors may be used
  to endorse or promote products derived from this software without specific
  prior written permission.
  
* If the source code is used in a published work, then proper citation of the source
  code must be included with the published work.
  
  
NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY THIS
LICENSE. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
DAMAGE.


.. _Github_Pages: https://moseleybioinformaticslab.github.io/icikt/
.. _pip: https://pip.pypa.io/
.. _git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git/
.. _numpy: http://www.numpy.org/
.. _scipy: https://scipy.org/scipylib/index.html
.. _docopt: http://docopt.org/
.. _Cython: https://cython.org/
