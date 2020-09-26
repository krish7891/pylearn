*******************************************************************************
ndarray.shape
*******************************************************************************
This array attribute returns a tuple consisting of array dimensions. It can also be used to resize the array.


*******************************************************************************
ndarray.ndim
*******************************************************************************
This array attribute returns the number of array dimensions.


*******************************************************************************
numpy.itemsize
*******************************************************************************
This array attribute returns the length of each element of array in bytes.

*******************************************************************************
numpy.flags
*******************************************************************************
The ndarray object has the following attributes. Its current values are returned by this function.

1 C_CONTIGUOUS (C)
The data is in a single, C-style contiguous segment

2 F_CONTIGUOUS (F)
The data is in a single, Fortran-style contiguous segment

3 OWNDATA (O)
The array owns the memory it uses or borrows it from another object

4 WRITEABLE (W)
The data area can be written to. Setting this to False locks the data, making it read-only

5 ALIGNED (A)
The data and all elements are aligned appropriately for the hardware

6 UPDATEIFCOPY (U)
This array is a copy of some other array. When this array is deallocated, the base array will be updated with the contents of this array
