import matplotlib.pyplot as plt
import numpy as np
x1 = (0, 10, 20, 30, 40, 50, 60)
y1 = (3.25, 4.04, 4.51, 5.01, 5.29, 5.65, 6.04)
plt.plot(x1, y1, 'k')
plt.title('График зависимости расхода от расстояния до сопла')
plt.xlabel('Расстояние до сопла [mm]')
plt.ylabel('Расход [г/с]')
plt.minorticks_on()
plt.grid()
plt.show()
