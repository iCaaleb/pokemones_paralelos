# Actividad de pokemones paralelos

## Descripción

Programa en python para obtener los datos de pokemones en paralelo utilizando la libreria threading y request

## Desarrollo de la práctica

1. Se importaron las librerias necesarias para el desarollo de la práctica.
2. Se creó la función que obtiene los datos del pokemon. Primeramente se hace un request a la PokeAPI y luego se refactorizan los datos para mostrarlos en consola.
3. Se hizo un manejo de errores en esa función para los errores y exepciones HTTP.
4. Se creó la función principal, donde están crearon los hilos para cada uno de los 50 pokemones aleatorios.
5. Se corrió la función principal y se comprobó que los resultados de salida fueran correctos.
