import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-20,20,5)
y=x**2

fig=plt.figure(figsize=(10,6))
plt.plot(y)
plt.show()