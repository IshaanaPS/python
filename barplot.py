import matplotlib.pyplot as plt

continents=["america","asia","ocenia","australia","antartica"]
area=["1234","3478","3704","9480","8302"]
plt.bar(continents,area,color="blue")
plt.xlabel("x asis")
plt.ylabel("y axis")
plt.title("areas of continet")
plt.show()