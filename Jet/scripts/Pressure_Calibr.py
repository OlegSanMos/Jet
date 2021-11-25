import jetFunctions as jet
import matplotlib.pyplot as plt
import numpy as np

y1 = []
x1 = [0,150]
Pa_calibrovka1 = jet.readJetData('00_Pa.txt')
y1.append(np.mean(Pa_calibrovka1[0]))       #np.mean - ср. знач
Pa_calibrovka2 = jet.readJetData('70_Pa.txt')
y1.append(np.mean(Pa_calibrovka2[0]))
plt.title('Калибровочный график зависимости показаний АЦП от давления')
plt.ylabel('Отчеты АЦП')
plt.xlabel('Давление')
print(np.polyfit(y1, x1, 1))
line1 = plt.plot(x1, y1, 'r', label = 'P= 0,4083*N - 334,7791 ')
plt.minorticks_on()
plt.legend()
plt.grid(which='major',linestyle = '--')
plt.grid(which='minor',linestyle = '--')

plt.show()
