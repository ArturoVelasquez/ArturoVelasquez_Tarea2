import numpy as np
import matplot.pyplot as plt

density = np.genfromtxt('densidad_sedov.txt')

r10 = density[:,10]
r60 = density[:,60]
r120 = density[:,120]

time = np.linspace(0,len(r10),len(r10)+1)

distance = np.array([10,60,120])

def graficador(r1,r2,r3,d,t):
	for i in range len(t):
		r = np.array([r1[i],r2[i],r3[i]])
		fig = plt.figure()
		plt.plot(d, r, '.-')
		fig.text(0.15,0.03,'tiempo = %f'%t[i])
		plt.title('Densidad explosion de Sedov')
		plt.savefig('tiempo_%f' %t[i])
		plt.cla()

graficador(r10,r60,r120,distance,time)

fig2=plt.figure()
plt.save(empty.png)

