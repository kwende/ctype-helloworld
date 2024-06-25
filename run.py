import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL('D:\\repos\\ctype-helloworld\\CTypeHelloWorld\\x64\\Debug\\Library.dll')

# Define the argument types and return type for the function
lib.fill_array_with_ones.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
lib.fill_array_with_ones.restype = None

# Create a NumPy array
size = 10
array = np.zeros(size, dtype=np.int32)

# Call the C function
lib.fill_array_with_ones(array.ctypes.data_as(ctypes.POINTER(ctypes.c_int)), size)

# Print the modified array
print(array)