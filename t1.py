import numpy as np
from pylab import*
import astropy.constants as ac
import scipy.integrate as si
global ax
global bx
global a
global b


a=np.loadtxt('sun_AM0.dat')
print type (a)
x=range(len(a))
y=range(len(a))
for i in range(len(a)):
    x[i]=a[i][0]#*0.001   #guardando longitudes de onda en unidades de micrometro
    y[i]=a[i][1]#*10**(6)       #guardando espectro de un cuerpo negro
xscale('log')
xlabel('$longitud \ de \ onda \  [um]$')
ylabel('$flujo [ ergs\cdot s^-1 \cdot cm^-2 \cdot um^-1]$')
plot(x,y)
grid(True)
title('$Radiacion \ de \ un \ cuerpo \ negro$')
savefig("radiacion.png")
show()

#parte 2

intT= 0
i=0
while i<(len(a)-1):
    delta=x[i+1]-x[i]
    intT += (y[i]+y[i+1])* (delta/2)
    i+=1
print "constante solar =",
print intT, "[W*m^-2]"


'''el valor que nos entrego la integral del trapecio es la cte solar
esta se debe multiplicar por 4*pi* au'''

Lumi=(4*np.pi)*((ac.au.value)**2)*intT
print "Luminosidad solar =",
print Lumi, "[W]"

comp=si.trapz(y,x)
print "valor con pc = ",
print comp




#Parte 3

h=ac.h
c=ac.c
k=ac.k_B
a=ac.a0
t=5778.0 #

def f(x):
    return (((np.tan(x))**3.0)*((np.cos(x))**(-2.0)))/(np.exp(np.tan(x))-1)

pini=((2*np.pi*h)/c**2)*((k*t)/h)**4
a=0.0000001 #para que no se indefina
b= np.pi/2
def inteplanck(x):
    a=0.0000001 #para que no se indefina
    b= np.pi/2 #por cambio de variable
    n=1000    #integral para la funcion
    esp=np.linspace(a,b,n)
    delta= (esp[1]-esp[0])/2
    c=0
    intp=0
    while c < n-2:
        intp += (delta/3.0)*(f(esp[c])+(4*f(esp[c+1]))+ f(esp[c+2]))
        c+= 1
    return intp

print "integral",
print inteplanck(f)
print "valor analitico",
print pini*(np.pi**4)/15
print "constante de planck",
print pini*(inteplanck(f))

com2=si.quad(f,a,b)
print "valor de la integral calculado por scipy = ",
print com2

#calcular el radio del sol
P=inteplanck(f)*pini
radio = np.sqrt(Lumi/(4*np.pi*P))
print "radio del sol = ",
print radio, "km"
