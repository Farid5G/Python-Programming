# how to generate a random data in numpy
import numpy as np
np_height = np.round(np.random.normal(1.72,2.11,100),2)
print(np_height)

# some numpy function 
# mean and median
print(f"Median height: {np.median(np_height)}")
print(f"Mean height: {round(np.mean(np_height),3)}")