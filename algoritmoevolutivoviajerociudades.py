# -*- coding: utf-8 -*-
"""AlgoritmoEvolutivoViajeroCiudades.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dJCjwY4-L538VvrQvdskJglJqjUiXPLs

Prueba 1)
"""

import random

# Definir las poblaciones
#poblaciones = ["Las Palmas", "Telde", "Gáldar", "Vecindario", "Teror", "Santa Lucía", "Maspalomas", "Agaete", "San Mateo"]
poblaciones = ["Las Palmas", "Telde", "Gáldar", "Vecindario", "Teror", "Santa Lucía", "Maspalomas", "Agaete"]

# Definir la matriz de distancias entre las poblaciones (valores ficticios, reemplazar con valores reales)
matriz_distancias = [
    # [0, 12, 30, 15, 18, 25, 40, 28, 22],  # Distancias desde Las Palmas a otras poblaciones
    # [12, 0, 22, 10, 20, 30, 35, 25, 18],  # Distancias desde Telde a otras poblaciones
    # [30, 22, 0, 28, 35, 40, 15, 10, 30],  # Distancias desde Gáldar a otras poblaciones
    # [15, 10, 28, 0, 14, 22, 18, 30, 25],  # Distancias desde Vecindario a otras poblaciones
    # [18, 20, 35, 14, 0, 12, 30, 25, 22],  # Distancias desde Teror a otras poblaciones
    # [25, 30, 40, 22, 12, 0, 20, 32, 28],  # Distancias desde Santa Lucía a otras poblaciones
    # [40, 35, 15, 18, 30, 20, 0, 14, 25],  # Distancias desde Maspalomas a otras poblaciones
    # [28, 25, 10, 30, 25, 32, 14, 0, 18],  # Distancias desde Agaete a otras poblaciones
    # [22, 18, 30, 25, 22, 28, 25, 18, 0]   # Distancias desde San Mateo a otras poblaciones


    [0, 12.7, 25.5, 19.3, 15.4, 51.5, 41.2, 21.1],  # Distancias desde Las Palmas a otras poblaciones
    [12.7, 0, 12.8, 7.6, 5.7, 38.7, 30.3, 18.8],    # Distancias desde Telde a otras poblaciones
    [25.5, 12.8, 0, 12.1, 9.2, 40.3, 31.9, 20.4],   # Distancias desde Gáldar a otras poblaciones
    [19.3, 7.6, 12.1, 0, 7.1, 36.1, 27.7, 16.2],    # Distancias desde Vecindario a otras poblaciones
    [15.4, 5.7, 9.2, 7.1, 0, 31.2, 22.8, 11.3],     # Distancias desde Teror a otras poblaciones
    [51.5, 38.7, 40.3, 36.1, 31.2, 0, 11.7, 38.6],  # Distancias desde Santa Lucía a otras poblaciones
    [41.2, 30.3, 31.9, 27.7, 22.8, 11.7, 0, 27.5],  # Distancias desde Maspalomas a otras poblaciones
    [21.1, 18.8, 20.4, 16.2, 11.3, 38.6, 27.5, 0]  # Distancias desde Agaete a otras poblaciones



]

# Función para generar una población inicial de rutas (índices de poblaciones)
def generar_poblacion(n_poblaciones):
    poblacion = []
    for _ in range(n_poblaciones):
        ruta = random.sample(range(n_poblaciones), n_poblaciones)
        poblacion.append(ruta)
    return poblacion

# Función para calcular la distancia total de una ruta
def calcular_distancia_total(ruta, matriz_distancias):
    distancia_total = 0
    for i in range(len(ruta) - 1):
        distancia_total += matriz_distancias[ruta[i]][ruta[i + 1]]
    distancia_total += matriz_distancias[ruta[-1]][ruta[0]]  # Volver a la primera población
    return distancia_total

# Función de evaluación de aptitud (menor distancia es mejor)
def evaluar_fitness(ruta, matriz_distancias):
    return -calcular_distancia_total(ruta, matriz_distancias)  # Negativo para que la menor distancia sea mejor

# Función de mutación
def mutar(individuo, p_mutacion):
    individuo_mutado = individuo.copy()
    if random.random() < p_mutacion:
        i, j = random.sample(range(len(individuo)), 2)
        individuo_mutado[i], individuo_mutado[j] = individuo_mutado[j], individuo_mutado[i]
    return individuo_mutado

# Función de recombinación
def recombinar(individuo_1, individuo_2):
    punto_de_corte = random.randint(0, len(individuo_1) - 1)
    nuevo_individuo_1 = individuo_1[:punto_de_corte] + [x for x in individuo_2 if x not in individuo_1[:punto_de_corte]]
    nuevo_individuo_2 = individuo_2[:punto_de_corte] + [x for x in individuo_1 if x not in individuo_2[:punto_de_corte]]
    return nuevo_individuo_1, nuevo_individuo_2

# Algoritmo genético con matriz_distancias como argumento adicional
def algoritmo_genetico(n_poblaciones, n_generaciones, p_mutacion, matriz_distancias):
    poblacion = generar_poblacion(n_poblaciones)
    for _ in range(n_generaciones):
        poblacion_ordenada = sorted(poblacion, key=lambda x: evaluar_fitness(x, matriz_distancias), reverse=True)
        poblacion = poblacion_ordenada[:n_poblaciones]
        for i in range(0, n_poblaciones, 2):
            individuo_1, individuo_2 = recombinar(poblacion[i], poblacion[i + 1])
            poblacion.append(individuo_1)
            poblacion.append(individuo_2)
        poblacion = [mutar(individuo, p_mutacion) for individuo in poblacion]
    return max(poblacion, key=lambda x: evaluar_fitness(x, matriz_distancias))

# Ejemplo de ejecución
n_poblaciones = len(poblaciones)
n_generaciones = 100
p_mutacion = 0.05

solucion = algoritmo_genetico(n_poblaciones, n_generaciones, p_mutacion, matriz_distancias)
distancia_solucion = -evaluar_fitness(solucion, matriz_distancias)  # Obtener la distancia positiva

print("Mejor ruta encontrada:", [poblaciones[i] for i in solucion])
print("Distancia de la mejor ruta:", distancia_solucion)

"""Prueba 2)"""

import random

# Definir las poblaciones y la matriz de distancias
#poblaciones = ["Las Palmas", "Telde", "Gáldar", "Vecindario", "Teror", "Santa Lucía", "Maspalomas", "Agaete", "San Mateo"]
poblaciones = ["Las Palmas", "Telde", "Gáldar", "Vecindario", "Teror", "Santa Lucía", "Maspalomas", "Agaete"]
matriz_distancias = [
    [0, 13, 26, 19, 15, 52, 41, 21],    # Distancias desde Las Palmas a otras poblaciones
    [13, 0, 12.8, 8, 6, 39, 30, 19],    # Distancias desde Telde a otras poblaciones
    [26, 13, 0, 12, 9, 40, 32, 20],     # Distancias desde Gáldar a otras poblaciones
    [19, 8, 12, 0, 7, 36, 28, 16],      # Distancias desde Vecindario a otras poblaciones
    [15, 6, 9, 7, 0, 31, 23, 11],       # Distancias desde Teror a otras poblaciones
    [52, 39, 40, 36, 31, 0, 12, 39],    # Distancias desde Santa Lucía a otras poblaciones
    [41, 30, 32, 28, 23, 12, 0, 28],  # Distancias desde Maspalomas a otras poblaciones
    [21, 19, 20, 16, 11, 39, 28, 0]   # Distancias desde Agaete a otras poblaciones
]

# Función para generar una población inicial de rutas (índices de poblaciones)
def generar_poblacion(n_poblaciones):
    poblacion = []
    for _ in range(n_poblaciones):
        ruta = random.sample(range(n_poblaciones), n_poblaciones)
        poblacion.append(ruta)
    return poblacion

# Función para calcular la distancia total de una ruta
def calcular_distancia_total(ruta, matriz_distancias):
    distancia_total = 0
    for i in range(len(ruta) - 1):
        distancia_total += matriz_distancias[ruta[i]][ruta[i + 1]]
    distancia_total += matriz_distancias[ruta[-1]][ruta[0]]  # Volver a la primera población
    return distancia_total

# Función de evaluación de aptitud (menor distancia es mejor)
def evaluar_fitness(ruta, matriz_distancias):
    return -calcular_distancia_total(ruta, matriz_distancias)  # Negativo para que la menor distancia sea mejor

# Función de mutación
def mutar(individuo, p_mutacion):
    individuo_mutado = individuo.copy()
    if random.random() < p_mutacion:
        i, j = random.sample(range(len(individuo)), 2)
        individuo_mutado[i], individuo_mutado[j] = individuo_mutado[j], individuo_mutado[i]
    return individuo_mutado

# Función de recombinación
def recombinar(individuo_1, individuo_2):
    punto_de_corte = random.randint(0, len(individuo_1) - 1)
    nuevo_individuo_1 = individuo_1[:punto_de_corte] + [x for x in individuo_2 if x not in individuo_1[:punto_de_corte]]
    nuevo_individuo_2 = individuo_2[:punto_de_corte] + [x for x in individuo_1 if x not in individuo_2[:punto_de_corte]]
    return nuevo_individuo_1, nuevo_individuo_2

# Algoritmo genético con matriz_distancias como argumento adicional
def algoritmo_genetico(n_poblaciones, n_generaciones, p_mutacion, matriz_distancias):
    poblacion = generar_poblacion(n_poblaciones)
    for _ in range(n_generaciones):
        poblacion_ordenada = sorted(poblacion, key=lambda x: evaluar_fitness(x, matriz_distancias), reverse=True)
        poblacion = poblacion_ordenada[:n_poblaciones]
        for i in range(0, n_poblaciones, 2):
            individuo_1, individuo_2 = recombinar(poblacion[i], poblacion[i + 1])
            poblacion.append(individuo_1)
            poblacion.append(individuo_2)
        poblacion = [mutar(individuo, p_mutacion) for individuo in poblacion]
    return max(poblacion, key=lambda x: evaluar_fitness(x, matriz_distancias))

# Indicar el punto de salida y el punto de llegada
punto_salida = "Las Palmas"
punto_llegada = "Maspalomas"

# Obtener índices de los puntos de salida y llegada en la lista de poblaciones
indice_salida = poblaciones.index(punto_salida)
indice_llegada = poblaciones.index(punto_llegada)

# Modificar la matriz de distancias para incluir solo las distancias entre el punto de salida y el punto de llegada
matriz_distancias = [fila[indice_salida:indice_llegada + 1] for fila in matriz_distancias[indice_salida:indice_llegada + 1]]

# Modificar la lista de poblaciones para incluir solo el punto de salida y el punto de llegada
poblaciones = poblaciones[indice_salida:indice_llegada + 1]

# Ejemplo de ejecución
n_poblaciones = len(poblaciones)
n_generaciones = 100
p_mutacion = 0.05

solucion = algoritmo_genetico(n_poblaciones, n_generaciones, p_mutacion, matriz_distancias)
distancia_solucion = -evaluar_fitness(solucion, matriz_distancias)  # Obtener la distancia positiva

# Imprimir la mejor ruta encontrada y la distancia de la mejor ruta
print("Mejor ruta encontrada:", [poblaciones[i] for i in solucion])
print("Distancia de la mejor ruta:", distancia_solucion)

"""Prueba 3)"""

import random
import heapq

# Definir las poblaciones y la matriz de distancias
poblaciones = ["Las Palmas", "Telde", "Gáldar", "Vecindario", "Teror", "Santa Lucía", "Maspalomas", "Agaete"]
matriz_distancias = [
    [0, 13, 26, 19, 15, 52, 41, 21],    # Distancias desde Las Palmas a otras poblaciones
    [13, 0, 12.8, 8, 6, 39, 30, 19],    # Distancias desde Telde a otras poblaciones
    [26, 13, 0, 12, 9, 40, 32, 20],     # Distancias desde Gáldar a otras poblaciones
    [19, 8, 12, 0, 7, 36, 28, 16],      # Distancias desde Vecindario a otras poblaciones
    [15, 6, 9, 7, 0, 31, 23, 11],       # Distancias desde Teror a otras poblaciones
    [52, 39, 40, 36, 31, 0, 12, 39],    # Distancias desde Santa Lucía a otras poblaciones
    [41, 30, 32, 28, 23, 12, 0, 28],    # Distancias desde Maspalomas a otras poblaciones
    [21, 19, 20, 16, 11, 39, 28, 0]     # Distancias desde Agaete a otras poblaciones
]

# Función para generar una población inicial de rutas (índices de poblaciones)
def generar_poblacion(n_poblaciones):
    poblacion = []
    for _ in range(n_poblaciones):
        ruta = random.sample(range(n_poblaciones), n_poblaciones)
        poblacion.append(ruta)
    return poblacion

# Función para calcular la distancia total de una ruta
def calcular_distancia_total(ruta, matriz_distancias):
    distancia_total = 0
    for i in range(len(ruta) - 1):
        distancia_total += matriz_distancias[ruta[i]][ruta[i + 1]]
    distancia_total += matriz_distancias[ruta[-1]][ruta[0]]  # Volver a la primera población
    return distancia_total

# Función de evaluación de aptitud (menor distancia es mejor)
def evaluar_fitness(ruta, matriz_distancias):
    return -calcular_distancia_total(ruta, matriz_distancias)  # Negativo para que la menor distancia sea mejor

# Función de mutación
def mutar(individuo, p_mutacion):
    individuo_mutado = individuo.copy()
    if random.random() < p_mutacion:
        i, j = random.sample(range(len(individuo)), 2)
        individuo_mutado[i], individuo_mutado[j] = individuo_mutado[j], individuo_mutado[i]
    return individuo_mutado

# Función de recombinación
def recombinar(individuo_1, individuo_2):
    punto_de_corte = random.randint(0, len(individuo_1) - 1)
    nuevo_individuo_1 = individuo_1[:punto_de_corte] + [x for x in individuo_2 if x not in individuo_1[:punto_de_corte]]
    nuevo_individuo_2 = individuo_2[:punto_de_corte] + [x for x in individuo_1 if x not in individuo_2[:punto_de_corte]]
    return nuevo_individuo_1, nuevo_individuo_2

# Algoritmo genético con matriz_distancias como argumento adicional
def algoritmo_genetico(n_poblaciones, n_generaciones, p_mutacion, matriz_distancias):
    poblacion = generar_poblacion(n_poblaciones)
    for _ in range(n_generaciones):
        poblacion_ordenada = sorted(poblacion, key=lambda x: evaluar_fitness(x, matriz_distancias), reverse=True)
        poblacion = poblacion_ordenada[:n_poblaciones]
        for i in range(0, n_poblaciones, 2):
            individuo_1, individuo_2 = recombinar(poblacion[i], poblacion[i + 1])
            poblacion.append(individuo_1)
            poblacion.append(individuo_2)
        poblacion = [mutar(individuo, p_mutacion) for individuo in poblacion]
    return max(poblacion, key=lambda x: evaluar_fitness(x, matriz_distancias))

# Función para encontrar la ruta más corta usando el algoritmo de Dijkstra
def encontrar_ruta_mas_corta(matriz_distancias, punto_salida):
    distancia = [float('inf')] * len(matriz_distancias)
    distancia[punto_salida] = 0
    cola_prioridad = [(0, punto_salida)]

    while cola_prioridad:
        costo_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if costo_actual > distancia[nodo_actual]:
            continue

        for vecino, peso in enumerate(matriz_distancias[nodo_actual]):
            if distancia[nodo_actual] + peso < distancia[vecino]:
                distancia[vecino] = distancia[nodo_actual] + peso
                heapq.heappush(cola_prioridad, (distancia[vecino], vecino))

    return distancia

# Indicar el punto de salida y el punto de llegada
punto_salida = "Las Palmas"
punto_llegada = "Maspalomas"

# Obtener índices de los puntos de salida y llegada en la lista de poblaciones
indice_salida = poblaciones.index(punto_salida)
indice_llegada = poblaciones.index(punto_llegada)

# Calcular la ruta más corta desde el punto de salida
distancias_desde_salida = encontrar_ruta_mas_corta(matriz_distancias, indice_salida)

# Imprimir la población de salida, la población de llegada y las distancias desde la población de salida
print("Población de salida:", poblaciones[indice_salida])
print("Población de llegada:", poblaciones[indice_llegada])
print("Distancia desde la población de salida:", distancias_desde_salida[indice_llegada])

# Calcular las rutas y distancias desde la población de salida
for i, distancia in enumerate(distancias_desde_salida):
    if i != indice_salida:
        ruta = []
        nodo_actual = i
        while nodo_actual != indice_salida:
            ruta.insert(0, poblaciones[nodo_actual])
            for vecino, peso in enumerate(matriz_distancias[nodo_actual]):
                if distancia == distancias_desde_salida[vecino] + peso:
                    nodo_actual = vecino  # ¡Actualizar el nodo actual!
                    break
        ruta.insert(0, poblaciones[indice_salida])
        print("Ruta hacia", poblaciones[i], ":", " -> ".join(ruta), "Distancia:", distancia)