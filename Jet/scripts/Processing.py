import jetFunctions as jet
import matplotlib.pyplot as plt
import numpy as np

Data1 = jet.readJetData('10_mm.txt')
Data2 = jet.readJetData('20_mm.txt')
Data3 = jet.readJetData('30_mm.txt')
Data4 = jet.readJetData('40_mm.txt')
Data5 = jet.readJetData('50_mm.txt')
Data6 = jet.readJetData('60_mm.txt')

y1 = np.array(Data1[0])
y2 = np.array(Data2[0])
y3 = np.array(Data3[0])
y4 = np.array(Data4[0])
y5 = np.array(Data5[0])
y6 = np.array(Data6[0])

y1 = np.array(Data1[0])
p1 = 0.4083 * y1 - 334.7791
u1=np.sqrt((2 * p1) / 1.2)
x1 = np.linspace(0, ((5.2 / 100)), 120) # массив из последовательности точе(start,stop, quaniti)
x1max = np.argmax(u1)                    # нахождение индекса максимального элемента массива(Вершина)
delta1 = x1[x1max]                       # Центровка
x1=x1 - delta1

q1 = 1.2 * 2 * np.pi * 0.000052 * 4 * 1000 * u1 * x1
q1 = np.sum(np.abs(q1)) / 2
print(q1, end = '\n ')

y2 = np.array(Data2[0])
p2 = 0.4083 * y2 - 334.7791
u2= np.sqrt((2 * p2) / 1.2)
x2 = np.linspace(0, ((5.2 / 100)), 120)
x2max = np.argmax(u2)
delta2 = x2[x2max]
x2 = x2 - delta2

q2 = 1.2 * 2 * np.pi * 0.000052 * 4 * 1000 * u2 * x2
q2 = np.sum(np.abs(q2)) / 2
print(q2, end= '\n ')

y3 = np.array(Data3[0])
p3 = 0.4083 * y3 - 334.7791
u3= np.sqrt((2 * p3) / 1.2)
x3 = np.linspace(0, ((5.2 / 100)), 120)
x3max=np.argmax(u3)
delta3=x3[x3max]
x3 = x3 - delta3

q3=1.2 * 2 * np.pi * 0.000052 * 4 * 1000 * u3 * x3
q3=np.sum(np.abs(q3)) / 2
print(q3, end = '\n ')

y4 = np.array(Data4[0])
p4 = 0.4083 * y4 - 334.7791
u4= np.sqrt((2 * p4) / 1.2)
x4 = np.linspace(0, ((5.2 / 100)), 120)
x4max = np.argmax(u4)
delta4 = x4[x4max]
x4 = x4 - delta4

q4 = 1.2 * 2 * np.pi * 0.000052 * 4 * 1000 * u4 * x4
q4 = np.sum(np.abs(q4)) / 2
print(q4, end = '\n ')

y5 = np.array(Data5[0])
p5 = 0.4083 * y5 - 334.7791
u5= np.sqrt((2 * p5) / 1.2)
x5 = np.linspace(0, (5.2 / 100), 120)
x5max = np.argmax(u5)
delta5 = x5[x5max]
x5 = x5 - delta5

q5 = 1.2 * 2 * np.pi * 0.000052 * 4 * 1000 * u5 * x5
q5 = np.sum(np.abs(q5)) / 2
print(q5, end = '\n ')

y6 = np.array(Data6[0])
p6 = 0.4083 * y6 - 334.7791
u6= np.sqrt((2 * p6) / 1.2)
x6 = np.linspace(0, (5.2 / 100), 120)
x6max = np.argmax(u6)
delta6 = x6[x6max]
x6 = x6 - delta6

q6 = 1.2 * 2 * np.pi * 0.000052 * 4 * 1000 * u6 * x6
q6 = np.sum(np.abs(q6)) / 2
print(q6, end = '\n ')

###################################################################
plt.figure(figsize=(10, 10))
plt.title('Скорость потока воздуха в сечении затопленной струи')
plt.xlabel('Положение трубки Пито относительно центра струи [мм]')
plt.ylabel('Скорость воздуха [м/с]')

plt.plot(x1, u1, color = 'g', label = 'Q1 (10 mm) = 4.04 [г/с]')
plt.plot(x2, u2, color = 'r', label = 'Q2 (20 mm) = 4.51 [г/с]')
plt.plot(x3, u3, color = 'c', label = 'Q3 (30 mm) = 5.01 [г/с]')
plt.plot(x4, u4, color = 'y', label = 'Q4 (40 mm) = 5.29 [г/с]')
plt.plot(x5, u5, color = 'm', label = 'Q5 (50 mm) = 5.65 [г/с]')
plt.plot(x6, u6, color = 'k', label = 'Q6 (60 mm) = 6.04 [г/с]')

plt.legend()
plt.minorticks_on()
plt.grid(which = 'major')
plt.grid(which = 'minor', linestyle = '--')

plt.show()
