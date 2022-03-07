import numpy as np
import matplotlib.pyplot as plt

x = np.array([1960, 1980, 2000, 2008, 2020])
y = np.array([62, 701,1362, 2918,2603])
plt.plot(x, y)
plt.title ("PIB")
plt.xlabel("Années")
plt.ylabel("PIB (en milliars de dollars)")
plt.show() # affiche la figure a l'ecran