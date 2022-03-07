import numpy as np
import matplotlib.pyplot as plt

x = np.array([1960, 1980, 2000, 2020])
y = np.array([46,55 ,61,67])
plt.plot(x, y)
plt.title ("Population")
plt.xlabel("Années")
plt.ylabel("Habitants (en millions")
plt.show() # affiche la figure a l'ecran