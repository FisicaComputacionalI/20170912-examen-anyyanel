#Se importan las librerias
import matplotlib.pyplot as plt
import numpy as np
#Se define la funcion
def f(t):
 return ( 2 * np.cos(t) + 2014)
#Ahora se define el intervalo que recorre y el ritmo al que se agregan los valores
t1 = np.arange (0.0, 12.0, 0.1)
plt.plot(t1, f(t1), 'c*')
#Guardamos la imagen en formato 'png'
plt.savefig('ejercicio2.png')
