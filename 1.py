import numpy as np
from pylab import*



a=np.loadtxt('sun_AM0.dat')
print type (a)
x=range(len(a))
y=range(len(a))
for i in range(len(a)):
    x[i]=a[i][0]*0.001  #guardando l.o y transformado a micrones
    y[i]=a[i][1]*10**(-4)       #guardando espectro


plot(x,y)
xscale('log')
#yscale('log')
xlabel('longitud de onda [micron]')
ylabel('radiacion[cgs]')
title('Radiacion de un cuerpo negro')
savefig("1.png")
show()

xmin=x[0]
xmax=x[len(x)-1]

def integral(y,x,paso):
    delta=(len (x)-1)/paso
    integr=y[0]
    i=0
    while i<(len (x)-1):
        integr += y[i]
        i += int(delta)
    return integr*(delta/2.0)


sol=integral(y,x,160)
print sol

