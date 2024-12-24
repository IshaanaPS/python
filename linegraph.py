import matplotlib.pyplot as plt 
import numpy as np

a=np.array([2,3])
b=np.array([9,8])
print(a, "\n", b)

print("innerproduct",np.inner(a,b))
print("outerproduct",np.outer(a,b))
print("crossproduct",np.cross(a,b))

x=np.array([[1,2,3],[4,3,2]])
y=np.array([[4,5,7],[2,8,9]])
print(x,"\n",y)
print("innerproduct",np.inner(x,y))
print("outerproduct",np.outer(x,y))
print("crossproduct",np.cross(x,y))



