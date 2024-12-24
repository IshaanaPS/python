import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

x=np.linspace(-10,10,1000)

y=f(x)

plt.plot(x,y)
plt.show()
