'''Copyright (c) 2001-2002 Enthought, Inc.  2003-2019, SciPy Developers.
   All rights reserved.

   Redistribution and use in source and binary forms, with or without
   modification, are permitted provided that the following conditions
   are met:

   1. Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.

   2. Redistributions in binary form must reproduce the above
      copyright notice, this list of conditions and the following
      disclaimer in the documentation and/or other materials provided
      with the distribution.

   3. Neither the name of the copyright holder nor the names of its
      contributors may be used to endorse or promote products derived
      from this software without specific prior written permission.

   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
   "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
   OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
   '''



# borrowed from scipy.stats._stats, cannot be imported as it is protected

# cython: profile=True
# cython: language_level=3
# define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
from cpython cimport bool
from libc cimport math
cimport cython
cimport numpy as np
from numpy.math cimport PI
from numpy.math cimport INFINITY
from numpy.math cimport NAN
from numpy cimport ndarray, int64_t, float64_t, intp_t

import warnings
import numpy as np
import scipy.stats, scipy.special
cimport scipy.special.cython_special as cs

@cython.wraparound(False)
@cython.boundscheck(False)
def kendall_dis(intp_t[:] x, intp_t[:] y):
    cdef:
        intp_t sup = 1 + np.max(y)
        # Use of `>> 14` improves cache performance of the Fenwick tree (see gh-10108)
        intp_t[::1] arr = np.zeros(sup + ((sup - 1) >> 14), dtype=np.intp)
        intp_t i = 0, k = 0, size = x.size, idx
        int64_t dis = 0

    with nogil:
        while i < size:
            while k < size and x[i] == x[k]:
                dis += i
                idx = y[k]
                while idx != 0:
                    dis -= arr[idx + (idx >> 14)]
                    idx = idx & (idx - 1)

                k += 1

            while i < k:
                idx = y[i]
                while idx < sup:
                    arr[idx + (idx >> 14)] += 1
                    idx += idx & -idx
                i += 1

    return dis
