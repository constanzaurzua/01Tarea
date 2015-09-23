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

ax=x[0] #valor min de las longitudes de onda
bx=x[len(x)-1] #valor max de las longitudes de onda
delta=(bx-ax)/(len(a)-1)
par=0
impar=0
i=1
while i<(len(a)-2):
        if i%2==1:
            impar+=y[i]
        elif i%2==0:
            par+=y[i]
        i+=1
        solsimp= (delta/3.0)*(y[0] + 4*impar + 2*par + y[len(x)-1])
print solsimp
