icikt
=====

Description
--------------
The ``icikt`` package provides a Python tool to calculate an information-content-informed 
Kendall Tau correlation coefficient between arrays, while also handling missing
values or values which need to be removed.

Full API documentation, user guide, and tutorial can be found on readthedocs_

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



GitHub Package installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Make sure you have git_ installed:

.. code:: bash

   git clone https://github.com/MoseleyBioinformaticsLab/pythonICIKendallTau.git

Dependencies
~~~~~~~~~~~~
``icikt`` requires the following Python libraries:
    * numpy_ and scipy_ for mathmatical calculations.
    * docopt_ for a command line interface.
    * Cython_ for optimized performance.

To install dependencies manually:

.. code:: bash

   pip3 install numpy
   pip3 install scipy
   pip3 install docopt
   pip3 install cython


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
        dataArray = numpy.random.randn(100, 2)

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


.. _readthedocs: https://icikt.readthedocs.io/en/latest/
.. _pip: https://pip.pypa.io/
.. _git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git/
.. _numpy: http://www.numpy.org/
.. _scipy: https://scipy.org/scipylib/index.html
.. _docopt: http://docopt.org/
.. _Cython: https://cython.org/
