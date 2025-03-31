"""
exercise: creating arrays

    task 1: create a one-dimensional array from a python list
    
    example: list [10, 20, 30, 40]
    
    task 2: generate a sequence of numbers using np.arange
    
    e.g., an array with values from 0 to 9
    
    task 3: create an array of 5 evenly spaced numbers between 0 and 1 with np.linspace
    
    task 4: create a two-dimensional array (shape 2x3) filled with zeros using np.zeros
    
    task 5: create a 3x3 identity matrix using np.eye
"""
import numpy as np

# Create a 2D array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(arr)

print(arr[1, 2])
