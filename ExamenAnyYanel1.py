#Se importa la libreria matplot para hacer la grafica y guardarla como imagen
import pylab as pl
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
y = [1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
pl.plot(x, y, 'bo')
#Colocamos las etiquetas para 'edad' y 'anio' a 'x' y 'y' respectivamente
pl.xlabel('edad')
pl.ylabel('anio')
#Se guarda la grafica en fomato 'png'
pl.savefig('AnyYanel1.png')
