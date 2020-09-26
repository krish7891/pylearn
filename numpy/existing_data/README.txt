*******************************************************************************
numpy.asarray
*******************************************************************************
This function is similar to numpy.array except for the fact that it has fewer parameters.
This routine is useful for converting Python sequence into ndarray.

Constructor : 
numpy.asarray(a, dtype = None, order = None)


*******************************************************************************
numpy.frombuffer
*******************************************************************************
This function interprets a buffer as one-dimensional array. Any object that exposes the buffer interface is used as parameter to return an ndarray.

numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)


*******************************************************************************
numpy.fromiter
*******************************************************************************
This function builds an ndarray object from any iterable object. A new one-dimensional array is returned by this function.

numpy.fromiter(iterable, dtype, count = -1)

