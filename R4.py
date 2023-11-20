#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from funciones import convierte, separador_miles

def r4():
    comunidadesFich=open("entradas/comunidadesAutonomas.htm", 'r', encoding="utf8")
    
    comString=comunidadesFich.read()
    soup = BeautifulSoup(comString, 'html.parser')
    
    celdas=soup.find_all('td')
    
    lista=[]
    aux = 0
    for celda in celdas:
        if aux==1:
            lista.append(celda.get_text())
            aux=0
        else:
            aux = 1
            
    comunidadesFich.close()
    
    comunidades={}
    
    for i in lista:
        comunidades[i]=[]
    
    mediaCom=open("resultados/poblacionComAutonomas.html", 'r', encoding="utf8")
    
    comString=mediaCom.read()
    soup = BeautifulSoup(comString, 'html.parser')
    celdas_p=soup.find_all('td')
    
    cont=0
    aux=-1
    
    for celda in celdas_p:  
        if cont == 0:
            aux+=1
        if cont > 7:
            try:
                l = comunidades[lista[aux]]
                l.append(float(convierte(celda.get_text())))
                comunidades[lista[aux]]=l
            except:
                m = celda
            
        cont+=1
        cont = cont % 24
    f = open("resultados/variacionComAutonomas.html",'w', encoding="utf8" )
    
    #Añadimos la cabecera
    paginaPob = """<!DOCTYPE HTML5><html>
    <head><title>Variacion Com.Autnomas</title>
    <link rel="stylesheet" href="../entradas/archivosAuxiliares/estilo.css">
    <meta charset="utf8"></head>
    <body><h1>Variación de la población  por comunidades autónomas</h1>"""
    
    cabecera_2 = "Comunidades;2017;2016;2015;2014;2013;2012;2011;2017;2016;2015;2014;2013;2012;2011;2017;2016;2015;2014;2013;2012;2011;2017;2016;2015;2014;2013;2012;2011"
    cabecera_2=cabecera_2.split(';')
    
    
    paginaPob+= """<table>
    <tr>
    <th></th>
    <th colspan="14">Variacion absoluta</th>
    <th colspan="14">Variacion relativa</th>
    </tr>
    <tr>
    <th></th>
    <th colspan="7">HOMBRES</th>
    <th colspan="7">MUJERES</th>
    <th colspan="7">HOMBRES</th>
    <th colspan="7">MUJERES</th>
    </tr>"""
    
    paginaPob+="<tr>"
    for nomColumna in cabecera_2:
        paginaPob+="<th>%s</th>" % (nomColumna)
    
    paginaPob+="</tr>"
    
    for fila in comunidades:
        #Pintamos el nombre de la comunidad
        paginaPob+="<tr><th>%s</th>" % (fila)
        
        L=comunidades[fila]
    
        for i in range(15):
            try:
                num = L[i]-L[i+1]
                num =  separador_miles(num,'i')
                paginaPob+="<td>%s</td>" % (str(num))
            except:
                m = num #extraigo errores
        for j in range(14):
            try:
                num = L[j]-L[j+1]
                num = (num / L[j+1])*100
                num =  separador_miles(num)
                paginaPob+="<td>%s</td>" % (str(num))
            except:
                m2 = num
    paginaPob+="</tr>"
    paginaPob+="</body></html>"
    
    f.write(paginaPob)
    f.close()
    return()