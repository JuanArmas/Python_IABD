# -*- coding: utf-8 -*-
"""Laberinto_DFS_prueba.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1meTCWDT9x8gA4MyXal2zS8i2rby1Aczn

# Laberinto__Juan Armas Alemán

# Explicacion del código.

<h1> Importación de bibliotecas y módulos

- Importa la biblioteca **matplotlib** para importar los módulos pyplot (que nos permitirá crear la visualización del laberinto) y al módulo **colors** para acceder a su submódulo, **ListedColorMap**, el cual nos dejará jugar con los colores del laberinto.

- Importa la biblioteca **numpy** que nos facilitará el uso de las distintas matrices bidimensionales y para las funciones que usaremos para la DFS.
"""

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

"""<h1> Creación de la clase Place

Crearemos objetos de tipo Place con coordenadas de fila y columna para almacenarlas como atributos del objeto para su uso
"""

class Place:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

"""<h1> Inicializamos Laberinto:

Creamos la matriz laberinto de 10x10 inicializado a cero.

Marcamos los bordes de dicho laberinto igualandolo a 1, de esta manera, más adelante indicaremos los colores según el valor de la casilla.

Finalmente pedimos a la función que nos devuelva el resultado para poder llamarla cuando haga falta.
"""

def inicializar_laberinto():
    laberinto = np.zeros((10, 10), dtype=int)
    laberinto[:, 0] = 1
    laberinto[:, -1] = 1
    laberinto[0, :] = 1
    laberinto[-1, :] = 1
    return laberinto

"""<h1> Definimos punto de inicio y de fin

A la función le pasamos por parámetro la matriz, y las coordenadas de inicio y de fin de recorrido. Esta función se encarga de reconocer esas coordenadas y asignarles un valor numérico para poder darle el color necesario en todo momento.
"""

def marcar_puntos_inicio_y_fin(laberinto, inicio, objetivo):
    laberinto[inicio] = 2
    laberinto[objetivo] = 3

"""<h1> Marcamos los obstáculos

La función de este método es igual que la del anterior. Le pasamos por parámetro la matriz y una lista de tuplas donde estarán reflejadas las coordenadas de cada muro interior, los cuales las igualamos a 1 dentro de este método para que tenga el color de un muro.
"""

def marcar_obstaculos(laberinto, obstaculos):
    for obstaculo in obstaculos:
        laberinto[obstaculo] = 1

"""<h1> Busqueda del camino óptimo

Aquí es donde recorreremos el laberinto usando DBFS (Búsqueda en profundidad) desde el punto de inicio hasta el punto objetivo.

"""

def encontrar_camino(laberinto, inicio, objetivo, visitados=None, intentos=0):
    if visitados is None:
        visitados = set()

    filas, columnas = len(laberinto), len(laberinto[0])
    fila, columna = inicio
    if (fila, columna) == objetivo:
        return [(fila, columna)], 1, 0

    move = [[0, -1], [1, 0], [0, 1], [-1, 0]]

    for nr, nc in move:
        nueva_fila, nueva_columna = fila + nr, columna + nc
        no_es_muro = laberinto[nueva_fila][nueva_columna] != 1
        fila_en_rango = 0 <= nueva_fila < filas
        columna_en_rango = 0 <= nueva_columna < columnas

        if fila_en_rango and columna_en_rango and no_es_muro and (nueva_fila, nueva_columna) not in visitados:
            visitados.add((nueva_fila, nueva_columna))
            camino, intentos_recursivos, pasos = encontrar_camino(laberinto, (nueva_fila, nueva_columna), objetivo, visitados, intentos+1)
            intentos += intentos_recursivos
            if camino:
                return [(fila, columna)] + camino, intentos, pasos + 1

    return [], intentos, 0

"""<h1> Creación visual del laberito:

- En este punto es donde se muestra de manera visual el laberinto y su recorrido, recibiendo por parámetro ellaberinto y el camino en caso de haber encontrado alguno en la función anterior.

detallo los puntos mas relevantes:

1)  se configuran los límites del laberinto con el xlim/ylim.

2) Se cuadricula todo el laberinto con el gca y pone marcas (x,y) en cada celda.Básicamente rueda 0.5 unidades tanto el eje x y el eje y para que cuando se muestre, no aparezca la marca en un lateral de la celda sino en el centro. (el centro entre -0.5 y 0.5, que son las marcas de las columnas o filas, es 0)

3) el condicional muestra el laberinto o un mensaje de error en caso de no haber encontrado ningún recorrido.
"""

def mostrar_laberinto(laberinto, camino=None):
    colorMap = ListedColormap(["white", "gray", "orange", "green"])
    plt.figure()
    plt.imshow(laberinto, cmap=colorMap)
    plt.xlim(-0.5, len(laberinto[0]) - 0.5)
    plt.ylim(-0.5, len(laberinto) - 0.5)
    plt.gca().set_xticks(np.arange(-0.5, len(laberinto[0]) - 0.5, 1), minor=True)
    plt.gca().set_yticks(np.arange(-0.5, len(laberinto) - 0.5, 1), minor=True)
    plt.grid(which="minor", color="black", linestyle='-', linewidth=1.09)

    if camino:
        for paso, (fila, columna) in enumerate(camino):
            plt.text(columna, fila, str("x"), ha='center', va='center', color='orange', fontsize=10, fontweight='bold')
    else:
        plt.text(len(laberinto[0]) // 2, len(laberinto) // 2, "No hay camino válido para llegar al punto final.", ha='center',
                 va='center', color='red', fontsize=12, fontweight='bold')

    plt.show()

"""<h1> Metodo Main para ejecutar todo y mostrar los resultados:

Aquí se inicializa el laberinto, se definen los puntos de inicio y fin (objetivo) y se crean los obstáculos.

Ejecuta la función encontrar_camino() para empezar la búsqueda en amplitud y se imprimen los resultados.
"""

def main():
    laberinto = inicializar_laberinto()

    # Puntos de inicio (naranja) y objetivo (verde)
    inicio = (8, 1)
    objetivo = (1, 8)
    # inicio = (1, 1)
    # objetivo = (8, 8)

    obstaculos = [(1, 5), (1, 7), (2, 1), (2, 3), (2, 4), (2, 5), (2, 7), (3, 7), (4, 1), (4, 2), (4, 3), (4, 4),
                  (4, 5), (4, 7), (6, 3), (6, 5), (6, 6), (6, 7), (6, 8), (7, 1), (7, 2), (7, 3), (7, 5), (8, 7)]

    marcar_puntos_inicio_y_fin(laberinto, inicio, objetivo)
    marcar_obstaculos(laberinto, obstaculos)

    camino, intentos, pasos = encontrar_camino(laberinto, inicio, objetivo)

    if camino:
        print(f"Se encontró un camino válido para llegar al punto final en {intentos} intentos.")
        print(f"El agente ha dado {pasos} pasos en este intento para llegar al punto final.")
        print("Desglose del recorrido del agente:")
        for paso, (fila, columna) in enumerate(camino):
            print(f"Paso {paso + 1}: Fila {fila}, Columna {columna}")
    else:
        print(f"No hay camino válido para llegar al punto final en {intentos} intentos.")

    mostrar_laberinto(laberinto, camino)

#if __name__ == "__main__":
main()