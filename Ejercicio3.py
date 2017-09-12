#Importamos las librerias
import matplotlib.pyplot as plt
import numpy as np
#Definimos la funcion
def f(t):
 return ((2 * np.cos(t)) + 2014)
#Insertamos los valores del primer ejercicio
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
y = [1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
#Arreglamos los intervalos
t1 = np.arange(0.0, 12.0, 0.1)
#Hacemos dos graficas
plt.subplot(121)
plt.plot(t1, f(t1), 'ko', x, y)
plt.subplot(122)
plt.plot(t1, f(t1), 'c*')
#Guardamos la imagen en formato 'png'
plt.savefig('ejecicio3.png')
