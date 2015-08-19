# Tarea nro. 1
## FI3104B - Metodos Numericos Para la Ciencia y la Ingenieria
#### Prof. Valentino Gonzalez

La temperatura effectiva de una estrella corresponde a la temperatura del cuerpo negro que mejor se ajusta a su espectro. El cuerpo negro que mejor se ajusta a nuestro Sol, tiene una temperatura aproximada de 5778 K.

1. El archivo `sun_AMO.dat` contiene el espectro del Sol, medido justo afuera de nuestra atmosfera, en unidades de *energia por unidad de tiempo por unidad de area por unidad de longitud de onda*. Lea el archivo y plotee el espectro del Sol (es decir, flujo vs. longitud de onda). Use la convencion astronomica para su plot, esto es, usar *cgs* para las unidades de flujo y *Angstrom* o *micron* para la longitud de onda. Recuerde anotar los ejes incluyendo las unidades.

	> __Ayuda.__
	- El modulo `numpy` contiene la rutina `numpy.loadtxt` que le puede ser util para leer el archivo.
	- Para plotear se recomienda usar el modulo `matplotlib`. Hay muchos ejemplos, con codigo incluido en el siguiente [link](http://matplotlib.org/gallery.html), en particular [este ejemplo sencillo](http://matplotlib.org/examples/pylab_examples/simple_plot.html) puede ser util.

2. Elija un metodo apropiado para integrar el espectro en longitud de onda y calcule la luminosidad total del sol (energia por unidad de tiempo total). Se pide que escriba su propio algoritmo para llevar a cabo la integracion, en el futuro usaremos librerias de libre disposicion.

3. La radiacion de un cuerpo negro en unidades de energia por unidad de tiempo por unidad de area por unidad de longitud de onda esta dada por la funcion de Planck:

	<img src='eqs/planck.png' alt='Plank' height='70'>

	(latex: $$B_\lambda(T) = \frac{2 \pi h c^2 / \lambda^5}{e^{hc / \lambda k_B T} - 1})

	donde h es la constante de Planck, c es la velocidad de la luz en el vacio, k<sub>B</sub> es la constante de Bolzmann, T es la temperatura del cuerpo negro y &lambda; es la longitud de onda.

	Integre numericamente la funcion de Planck para estimar la energia total por unidad de area emitida por un cuerpo negro con la temperatura efectiva del sol (escriba su propio algoritmo). Comparela con la energia total calculada en 2) para estimar el radio efectivo del sol.

	>__Nota__. Se puede demostrar que la integral de la funcion de Planck corresponde a:

	><img src='eqs/planck_integrated.png' alt='Plank Integrated' height='70'>

	>(latex: $$P = \frac{2 \pi h}{c^2}\left( \frac{k_B T}{h} \right)^4 \int_0^\infty \frac{x^3}{e^x - 1}$$)

	>Y la integral se puede calcular analiticamente con resultado &pi;<sup>4</sup>/15. El problema pide elegir un metodo apropiado y calcular la integral numericamente y comparar con el resultado analitico.

	>__Ayuda.__
	- El modulo `astropy` contiene el submodulo `astropy.constants` que incluye todas las constantes necesarias ademas de rutinas para cambiar unidades.
	- La integral que es necesario calcular es entre 0 e &infin; asi que requiere ser normalizada. Intente el cambio de variable y=arctan(x).
	- Implemente un algoritmo que permita ir refinando el valor de la integral con una tolerancia elegida por Ud.

4. El modulo `scipy` en Python incluye los metodos `scipy.integrate.trapz` y `scipy.integrate.quad`. Utilicelos para re-calcular las integrales calculadas en 2. y 3. Compare los valores obtenidos y la velocidad de ejecucion del algoritmo escrito por Ud. vs. `scipy` ¿A que se debe la diferencia?

	>__Ayuda.__

	>En la consola `ipython` existe la `ipython magic` `%timeit` que permite estimar velocidad de ejecucion de funciones.


__Otras Notas.__
- Utilice `git` durante el desarrollo de la tarea para mantener un historial de los cambios realizados.
- La tarea se entrega como un *pull request* en github. El *pull request* debe incluir todos los codigos usados ademas de su informe.
- El informe puede ser entregado en cualquier formato que desee, este debe ser claro sin informacion ni de mas ni de menos.
