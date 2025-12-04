/* Subsetting Numpy Arrays */
import numpy as np
print (hello);

np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])

/* Two Dimensional NumPy Array */

Subsetting in 2D-Array is done as follows:  
np2d = ([
  [100, 200, 3000, 400, 500],  // 0
  [600, 700, 800, 900, 990]    // 1
])  

arr2dArray[rows : columns ] ==> // remember
np2d[: , 1:3] -->  return all rows and 1 and 2 column values from all rows

// In order to find 50th element from 2D numpy array we have to do following thing:  
print(numpy_array[: , 49])   ==> all rows and 49th index element will return 50th element  

// To convert a normal list into numPy array in python:  
a = [1,2,3,4]
numpy_array = np.array(a);  

import pyplot.matplotlib as plt
plt.clf() ==> clears the most recent plot you created
plt.show() ==>  will show the plot you created  
plt.text([20,40], "Histogram" ) ==>  will replace the 20, 40 to "Histogram text"
