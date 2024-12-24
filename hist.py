import matplotlib.pyplot as plt
import numpy as np

x=np.random.normal(170,10,250)
#x=int(input("enter the number of students: \n"))

plt.hist(x,color="green",edgecolor="black")
plt.show()

