import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10, 10))
y1 =[0, 0.0052]
x1=[0, 100]
plt.title('Калибровочный график зависимости перемещения трубки Пито от шага двигателя')
plt.ylabel('Перемещение трубки Пито [см]')
plt.xlabel('Количество шагов')
print(np.polyfit(x1, y1, 1)) # нахождение полиномиальной зависимости со степенью подгонки 1
grafic = plt.plot(x1, y1 , 'r', label = 'y=5,2e-05*step[M]')
plt.minorticks_on()
plt.legend()
plt.grid( which='major', linestyle = '--' )
plt.grid( which='minor', linestyle = '--' )

plt.show()