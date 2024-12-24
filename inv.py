import numpy as np

arr1=np.array([[1,3,4],[2,3,6],[7,4,1]])

print(arr1)

if np.linalg.det==0:
    print("no inverse ")
else:
  result=np.linalg.inv(arr1)
  print(result)