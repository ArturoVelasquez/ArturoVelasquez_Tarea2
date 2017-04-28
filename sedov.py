import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

density = np.genfromtxt('Density_sedov.data', delimiter=',')

r10 = density[:,5]
r60 = density[:,30]
r120 = density[:,60]

#time = np.linspace(0,len(r10),len(r10)+1)
time = np.genfromtxt('Times_sedov.data', delimeter=',')
distance = np.array([10,60,120])

def graficador(r1,r2,r3,d,t):
	for i in range (0,len(r1)):
		r = np.array([r1[i],r2[i],r3[i]])
		fig = plt.figure()
		plt.plot(d, r, '.-')
		fig.text(0.15,0.03,'tiempo = %f'%t[i])
		plt.title('Densidad explosion de Sedov')
		plt.savefig('tiempo_%d'%t[i])
		plt.close()

graficador(r10,r60,r120,distance,time)


