import os
import time
import random
import sys
MI_MAPA = [
    ["#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", ".", ".", ".", "#"],
    ["#", ".", "#", "#", "#", ".", ".", "#"],
    ["#", ".", "#", "S", "#", ".", "#", "#"],
    ["#", ".", ".", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#"]
]
POS_INICIAL_RATON = [1, 1]
POS_INICIAL_GATO = [1, 6]

def distancia(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def obtener_movimientos(pos, mapa, es_gato=False):
    #Si es_gato es True, la función prohibira entrar en la salida 'S'.
    fila_actual, columna_actual = pos
    opciones_validas = []
    instrucciones = [(-1, 0), (1, 0), (0, -1), (0, 1)] #Para aclararme a mi mismo: arriba, abajo, izquierda y derecha 

    for d1, d2 in instrucciones:
        nueva_f = fila_actual + d1
        nueva_c = columna_actual + d2

        if 0 <= nueva_f < len(mapa) and 0 <= nueva_c < len(mapa[0]):
            contenido = mapa[nueva_f][nueva_c]
            
            # El raton puede ir a cualquier lado que no sea pared
            if not es_gato and contenido != "#":
                opciones_validas.append([nueva_f, nueva_c])
            
            #El gato NO puede entrar en pared (#) ni en salida (S)
            elif es_gato and contenido != "#" and contenido != "S":
                opciones_validas.append([nueva_f, nueva_c])

    return opciones_validas

def dibujar(mapa, p_raton, p_gato):
    os.system('cls' if os.name == 'nt' else 'clear')
    tablero = [fila[:] for fila in mapa]
    tablero[p_raton[0]][p_raton[1]] = "R"
    tablero[p_gato[0]][p_gato[1]] = "G"
    for fila in tablero:
        print(" ".join(fila))
    print("-" * 20)
    
#logica(MINIMAX SIMPLE)
def simular():
    raton = POS_INICIAL_RATON
    gato = POS_INICIAL_GATO
    turnos = 0

    while True:
        turnos += 1
        
        # MOVIMIENTO DEL RATON (MAXIMIZA DISTANCIA)
        pasos_r = obtener_movimientos(raton, MI_MAPA, es_gato=False)
        if pasos_r:
            # Si puede ganar, gana
            salida = [p for p in pasos_r if MI_MAPA[p[0]][p[1]] == "S"]
            if salida:
                raton = salida[0]
            else:
                # Si no, busca el paso que mas le aleje del gato
                d_max = -1
                mejores_pasos = []
                for p in pasos_r:
                    d = distancia(p, gato)
                    if d > d_max:
                        d_max = d
                        mejores_pasos = [p]
                    elif d == d_max:
                        mejores_pasos.append(p)
                raton = random.choice(mejores_pasos)

        dibujar(MI_MAPA, raton, gato)
        if MI_MAPA[raton[0]][raton[1]] == "S":
            print(f"¡VICTORIA! El ratón escapó en {turnos} turnos.")
            break
        
        # COLISION
        if raton == gato:
            print(f"DERROTA! El ratón se entrego al gato en el turno {turnos}.")
            break
        time.sleep(0.6)

        # GATO (MINIMIZA DISTANCIA)
        # es_gato=True para activar la restriccion de la salida
        pasos_g = obtener_movimientos(gato, MI_MAPA, es_gato=True)
        if pasos_g:
            d_min = float('inf')
            mejor_g = pasos_g[0]
            for p in pasos_g:
                d = distancia(p, raton)
                if d < d_min:
                    d_min = d
                    mejor_g = p
            gato = mejor_g

        dibujar(MI_MAPA, raton, gato)
        if raton == gato:
            print(f"DERROTA! El gato atrapo al raton en el turno {turnos}.")
            break
        time.sleep(0.6)

if __name__ == "__main__":
    simular()