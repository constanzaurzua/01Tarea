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

#Parte 3
import astropy.constants as ac
h=ac.h.cgs
c=ac.c.cgs
k=ac.k_B.cgs
T=5778 #

def f(x):
    return ((np.tan(x))**3*(1/np.cos(x))**2)/(np.exp(np.tan(x))-1)


'''funcion que me dará la integral esta funcion se indefine con a=0 y b= pi/2 por lo que debe aplicar el metodo del punto medio'''

#x_values = np.linspace(0, np.pi, 100)
#plot(x_values,f)
#show()
pini=((2*np.pi*h)/c**2)*((k*T)/h)**4.0
'''esta es la primera parte de la integral'''
def intesimpsons(n):
    '''n es el numero de divisiones al integrar y esta funcion lo que hace es hacer la integracion a
    a traves del metodo de simpsons'''

    delta (b-a)/n
    par=0.0
    impar=0.0
    i=0.0
    for i in range(1,n):
        if f(i)%2==1:
            impar+=f(i)
        elif f(i)%2==0:
            par+=f(i)
        i+=1
    return (delta/3.0)*(f(a)+4*impar + 2*par + f(b) )

solf= pini*intesimpsons(1000)
