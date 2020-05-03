import cupy as cp
import numpy as np
print('starting')
x= np.array([1, 2, 3, 4])
print(x)
gpu_x = cp.array(x)
print(gpu_x)
print('starting')