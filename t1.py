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


xscale('log')
xlabel('$longitud \ de \ onda \  [um]$')
ylabel('$flujo [ ergs\cdot s^-1 \cdot cm^-2 \cdot um^-1]$')
plot(x,y)
grid(True)
title('$Radiacion \ de \ un \ cuerpo \ negro$')
savefig("radiacion.png")
#show()

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

#haciendo sipmsons


delta=(bx-ax)/(len(a)-1)
par=0
impar=0
i=0
while i<(len(a)-1):
        if i%2==1:
            impar+=y[i]
        elif i%2==0:
            par+=y[i]
        i+=1
        solsimp= (delta/3.0)*(y[0] + 4*impar + 2*par + y[(len(x)-1)])
print solsimp

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
        if i==1:
            b=i
            a=0
            pmi=(b-a)*f((a+b)/2)
        elif i==n-1 :
            a=i
            b=np.pi/2
            pmf=(b-a)*f((a+b)/2)
        elif i%2==1:
            impar+=f(i)
        elif i%2==0:
            par+=f(i)
    return (delta/3.0)*(4*impar + 2*par) + pmi + pmf

intesimpsons(1000)*pini
