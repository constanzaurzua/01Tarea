import numpy as np
from pylab import*
import math
global ax
global bx
global a
global b



a=np.loadtxt('sun_AM0.dat')
print type (a)
x=range(len(a))
y=range(len(a))
for i in range(len(a)):
    x[i]=a[i][0]*0.001   #guardando longitudes de onda en unidades de micrometro
    y[i]=a[i][1]*10**(6)       #guardando espectro de un cuerpo negro

#Parte 3

import astropy.constants as ac

h=ac.h.cgs
c=ac.c.cgs
k=ac.k_B.cgs
T=5778 #

def f(x):
    return (((np.tan(x))**3.)*((np.cos(x))**(-2.0)))/(np.exp(np.tan(x))-1)

pini=((2*np.pi*h)/c**2)*((k*T)/h)**4.0

a=0#lim inicial
b= np.pi/2#lim final
def intesimpsons(n):
    a=0#lim inicial
    b= np.pi/2#lim final
    delta=(b-a)/n
    par=0
    impar=0
    i=0
    for i in range(1,n):
        x=a+i*delta
        if i==1:
            pmi=(x-a)*f((a+x)/2)
        elif i==n-1 :
            pmf=(b-x)*f((x+b)/2)
        elif i%2==1:
            impar+=f(a+i*delta)
        elif i%2==0:
            par+=f(a+i*delta)
    return (delta/3.0)*(4*impar + 2*par) + pmi + pmf

intesimpsons(1000)*pini
