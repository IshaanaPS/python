import numpy as np

a=np.array([[6,1,1,3],[4,-1,4,5],[2,7,8,6],[9,3,-8,1]])
print(a)

q,r=np.linalg.qr(a)
print("\n q: ",q)
print("\n r: ",r)
