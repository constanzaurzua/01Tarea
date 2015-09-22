import numpy as np
from pylab import*
import math
global ax
global bx


a=np.loadtxt('sun_AM0.dat')
print type (a)
x=range(len(a))
y=range(len(a))
for i in range(len(a)):
    x[i]=a[i][0]*0.001   #guardando longitudes de onda en unidades de micrometro
    y[i]=a[i][1]*10**(6)       #guardando espectro de un cuerpo negro


xscale('log')
xlabel('$longitud \ de \ onda \  [um]$')
ylabel('$flujo [ ergs\cdot s^-1 \cdot cm^-2 \cdot um^-1]$')
plot(x,y)
grid(True)
title('$Radiacion \ de \ un \ cuerpo \ negro$')
savefig("radiacion.png")
show()

#parte 2



ax=x[0] #valor min de las longitudes de onda
bx=x[len(x)-1] #valor max de las longitudes de onda
delt=(bx-ax)/(len(a)-1)
integr=  y[0]
i=0
while i<(len(a)-1):
    integr += y[i]
    i +=1
    sol=(2.0*integr+ y[0] + y[len(x)-1])*(delt/2.0)


print sol

#Parte 3
import astropy
import astropy.constants as ac


def f(x):'''a priori la funcion era impropia pero como no se puede dar solucion a una funcion impropia
cambio de variable y =arctan(x) en donde x->0 ; y->0 si x->inf y->pi/2'''
    P= ((np.tan(x))**3.0*((np.tan(x))**2+1))/(np.exp(np.tan(x))-1)
    return p
b=np.pi/2.0
a=  0.0
def intsimpsons(n):
    '''n es el numerode divisiones que le daremos'''
    delta=(b-a)/n
    par=0.0
    impar=0.0
    for i in range(1,n):
        if f(i) % 2 == 0:
            par +=f(i)
        elif f(i)% 2 == 1:
            impar+=f(i)
        i+=1
    sol=(delta/3.0)*(f(a)+4*impar+2*par+f(b))
    return sol

integral=intsimpsons(n) #tengo que ingresar la mejor aproximacion

pi=np.pi
h=ac.h.cgs
c=ac.h.cgs
k=ac.k_B.cgs
T=5778.0 #grados kelvin temperatura del sol

pi=((np.pi*h)/c**2.0)*(k*t/h)**4'''parte inicial de la integral'''
intplanck= partei*integral
