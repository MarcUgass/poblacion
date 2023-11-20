#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from funciones import poblacioncomunidad, urltabla
import matplotlib.pyplot as plt
import numpy as np

def r3():
    lista = urltabla("entradas/comunidadesAutonomas.htm")
        
    diccionario = {}
    for i in range(0, len(lista), 2):
        clave = lista[i].strip().replace(" - ", "-") + ' ' + lista[i + 1] #Castilla - La Manxa a Castilla-La Manxa, ya que no son iguales
        diccionario[clave] = []
        
    lista = urltabla("entradas/comunidadAutonoma-Provincia.htm")
    dicc = poblacioncomunidad(lista, diccionario, 3)
    diccmed = {}
    
    for clave, valores in dicc.items():
        media1 = sum(valores[:8]) / (len(valores)/2)
        media2 = sum(valores[8:16]) / (len(valores) /2)
        diccmed[clave] = []
        diccmed[clave].append(media1)
        diccmed[clave].append(media2)
        
    diccionario_ordenado = dict(sorted(diccmed.items(), key=lambda x: x[1]))
    # [[HAn,MAn], [HAr.Mar],...]
    hombres = []
    mujeres = []
    claves = []
    
    for comunidad, habitantes in diccionario_ordenado.items():
        hombres.append(diccionario_ordenado[comunidad][0])
        mujeres.append(diccionario_ordenado[comunidad][1])
        claves.append(comunidad)
        
    hgrafica = hombres[9:19]
    mgrafica = mujeres[9:19]
    hgrafica.reverse()
    mgrafica.reverse()
    
    x = np.arange(len(claves))
    

    plt.figure("barras")
    plt.axis([0, 10, 0, 5000000])
    plt.bar(x + 0.00, hgrafica[0], color = "b", width = 0.25)
    plt.bar(x + 0.25, mgrafica[1], color = "r", width = 0.25)
    plt.xticks(x+0.38, claves)
    # Mostrar la gráfica
    plt.savefig("imagenes/R3.png")
    
    
    return()
