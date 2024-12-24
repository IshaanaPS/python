import pandas as p
import numpy as np


arr=np.arange(1,11).reshape(2,5)
print(arr)

DF=p.DataFrame(arr)
DF.to_csv("data1.csv")

