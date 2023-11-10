import numpy as np
weight = [34,54,64]
height = [134,154,164]
np_weight = np.array(weight)
np_height = np.array(height)

bmi = np_weight / np_height  ** 2
print(bmi)