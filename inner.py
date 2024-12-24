import numpy as np

a=np.array([2,6])
b=np.array([3,5])
print("vectors")
print("a=",a)
print("b=",b)


print("inner product of a and b are:",np.inner(a,b))
print("outer product of a and b are:",np.outer(a,b))
print("cross product of a and b are:",np.outer(a,b))

x=np.array([[1,2,3],[45,6,9],[7,9,3]])
y=np.array([[2,4,6],[4,9,7],[2,4,9]])

print("inner product of a and b are:",np.inner(x,y))
print("outer product of a and b are:",np.outer(x,y))
print("cross product of a and b are:",np.outer(x,y))

