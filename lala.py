import matplotlib.pyplot as plt
import numpy as np

def f(x):

    '''a priori la funcion era impropia pero como no se puede dar solucion a una funcion impropia
cambio de variable y =arctan(x) en donde x->0 ; y->0 si x->inf y->pi/2'''
    return ((np.tan(x))**3*(1/np.cos(x))**2)/(np.exp(np.tan(x))-1)

b=np.pi/2.0
a=  0
print f(np.pi/4)

#((tan(y)**3)*((1/cos(y))**2))/(exp(tan(y))-1)
#((np.tan(x))**3*(1/np.cos(x))**2)/(np.exp(np.tan(x))-1)
