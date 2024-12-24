import numpy as np

m1=np.arange(3*4*4).reshape(3,4,4)
print("original matrix \n",m1)

diag_array=np.diagonal(m1,axis1=1,axis2=2)
print("diagonal matrix \n",diag_array)