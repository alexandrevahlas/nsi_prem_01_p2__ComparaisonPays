import numpy as np
import matplotlib.pyplot as plt

x = np.array([1990, 2000, 2008, 2020])
y = np.array([554, 259, 1661,1483])
plt.plot(x, y)
plt.title ("PIB")
plt.xlabel("Années")
plt.ylabel("PIB (en milliars de dollars)")
plt.show() # affiche la figure a l'ecran