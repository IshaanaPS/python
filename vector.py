import numpy as np

a=np.arange(2*3*3).reshape(2,3,3)
b=np.arange(2*3*3).reshape(2,3,3)
print("vectors\n")
print("a=",a)
print("\nb=",b)

print("inner products of vector a and b ara\n")
print(np.inner(a,b))
print("outer products of vector a nd b are\n")
print(np.outer(a,b))
print("cross product of vector a and b are\n")
print(np.cross(a,b))
