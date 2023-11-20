#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
from bs4 import BeautifulSoup
import locale

def poblacioncomunidad(lista, diccionario, opcion): 
    combinada = []
    for i in range(1, len(lista), 2):
        if i < 200:
            numero = lista[i - 1 ]
            nombre = lista[i]
            combinada.append(f'{numero} {nombre}')
        elif i > 201: #hay un caso que no es igual a todos
            numero = lista[i]
            nombre = lista[i + 1]
            combinada.append(f'{numero} {nombre}')
            

    # Clasificar las provincias según el diccionario
    #peta a ciudades autnonomas al final del fitxer htm, mira la pagina web
    lon = len(combinada) - 1
    for i in range(0, lon , 2):
        clave = combinada[i]
        provincia = combinada[i+1]
        if clave in diccionario:
            diccionario[clave].append(provincia)
    
    #poblacionProvinciasHM2010-17.csv, datos de poblacion por provincia
    dicthab = csvtabla("entradas/poblacionProvinciasHM2010-17.csv", opcion)
    del dicthab["Total Nacional"]
    
    diccFinal = {}
    for comunidad, provincias1 in diccionario.items():
        try:
            habitantes_por_año = [0] * len(dicthab[provincias1[0]])  # Inicializar lista con ceros

            for provincia1 in provincias1:
                habitantes_provincia = dicthab.get(provincia1, ['0'] * len(habitantes_por_año))
                habitantes_provincia = [float(h) if h.strip().replace('.', '').isdigit() else 0 for h in habitantes_provincia]
                habitantes_por_año = [a + b for a, b in zip(habitantes_por_año, habitantes_provincia)]

            diccFinal[comunidad] = habitantes_por_año
        except:
            diccFinal[comunidad] = [0]*7
    
    return diccFinal

def csvtabla(archivo, opcion): #opcion depende de si quieres coger solo el total (opcion 1) o todo (opcion 2)
    ficheroInicial=open(archivo,"r", encoding="utf8")
    
    cadenaInicial = ficheroInicial.read()

    ficheroInicial.close()
    
    primero=cadenaInicial.find("Total Nacional")
    ultimo=cadenaInicial.find("Notas")

    cadenaFinal=cadenaInicial[primero:ultimo]
    
    ficheroFinal=open("FinalpoblacionProvinciasHM2010-17.csv","w",encoding="utf8")
    
    #cabecera="Provincia;2017;2016;2015;2014;2013;2012;2011;2010"
    
    ficheroFinal.write(cadenaFinal)
    
    ficheroFinal.close()
    dicc = {}
    with open("FinalpoblacionProvinciasHM2010-17.csv", encoding="utf8") as csvarchivo: #otra opcion para solo hombres y mujeres
        poblacionDict = csv.reader(csvarchivo, delimiter=';')     
        for regD in poblacionDict:
            if opcion == 1:
                for i in range(9):
                    if i == 0:
                        dicc[regD[0]] = []
                    else:
                        dicc[regD[0]].append(regD[i])
            elif opcion == 2:
                for i in range(25):
                    if i == 0:
                        dicc[regD[0]] = []
                    else:
                        dicc[regD[0]].append(regD[i])
            elif opcion ==3:
                for i in range(17):
                    if i == 0:
                        dicc[regD[0]] = []
                    else:
                        dicc[regD[0]].append(regD[i+8])
    return dicc
    
def urltabla(url):


    comunidadesFich=open(url, 'r', encoding="utf8")

    comString=comunidadesFich.read()

    soup = BeautifulSoup(comString, 'html.parser')

    celdas=soup.find_all('td')


    listaValores=[]

    
    for celda in celdas:
        listaValores.append(celda.get_text())
        
    return listaValores

def separador_miles(num,t='f'):

    locale.setlocale(locale.LC_ALL,'')
    if t=='i':
        return(locale.format_string('%.0f', num, grouping=True))
    else:
        return(locale.format_string('%.2f', num, grouping=True))

def convierte(num):
    l = num.split('.')
    cadena =''
    for i in l:
        cadena+=i
        
    return(cadena)