import numpy as np

m1=np.array([[1,2],[4,5]])
m2=np.array([[7,3],[6,9]])
print(m1)
print(m2)

result=np.einsum("mk,kn",m1,m2)
print("the einstein summation: ")
print(result)