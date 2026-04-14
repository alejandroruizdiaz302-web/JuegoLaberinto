Simulación Inteligente: Gato vs Ratón 

Descripción
Este proyecto es una simulación por turnos en consola de una persecución en un laberinto bidimensional. Está desarrollado completamente en Python y utiliza lógica matemática de Inteligencia Artificial para que ambos personajes tomen decisiones óptimas de movimiento en tiempo real.

Lógica y Algoritmos (Minimax)
El núcleo del juego utiliza una aproximación al algoritmo **Minimax**, calculando la **Distancia de Manhattan** entre las coordenadas de ambos personajes:

* **El Ratón (Maximizador):** Escanea sus movimientos válidos y busca el camino que **maximice** su distancia respecto al gato (sobrevivir) o busca la casilla de salida (`S`) para ganar.
* **El Gato (Minimizador):** Escanea sus opciones y busca **minimizar** la distancia hacia el ratón, eligiendo siempre el camino más directo para acorralarlo.
* **Aleatoriedad estratégica:** Si existen múltiples caminos igual de óptimos, los personajes eligen uno al azar utilizando `random.choice()` para simular fintas y movimientos naturales.

* lo que mas me costo es que el pinche raton se queria salir del mapa y el gato entraba en la "S".
