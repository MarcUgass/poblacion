#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from funciones import poblacioncomunidad, urltabla

def r2():
    #comunidadesAutonomas.html, sacar listado de comunidades
    lista = urltabla("entradas/comunidadesAutonomas.htm")
        
    diccionario = {}
    for i in range(0, len(lista), 2):
        clave = lista[i].strip().replace(" - ", "-") + ' ' + lista[i + 1]
        #clave = lista[i].strip() + ' ' + lista[i + 1] 
        diccionario[clave] = []
        
    
    #comunidadAutonoma-Provincia.html, relacon de comunidad con provincia
    lista = urltabla("entradas/comunidadAutonoma-Provincia.htm")
    diccFinal = poblacioncomunidad(lista, diccionario, 2)
    #poblacionComAutonomas.html, creacion del fichero
    fileEstilo=open("entradas/estilo.css","w", encoding="utf8")

    estilo="""  table, th, td {
                border-collapse: collapse;    
                border:1px solid black;
                font-family: Arial, Helvetica, sans-serif;
                padding: 8px;
                
            }  """

    fileEstilo.write(estilo)
    fileEstilo.close()
            
            
    file=open("resultados/poblacionComAutonomas.html","w", encoding="utf8")
    
    paginaPob = """<!DOCTYPE html><html>
    <head><title>Población</title>
    <link rel="stylesheet" href="entradas/estilo.css">
    <meta charset="utf8"></head>
    <body><h1>Población Comunidades Auntonomas entre 2010-2017</h1>"""
    
    paginaPob+= """<p><table>
    <tr>"""
    
    cabecera = "<td colspan = 1> </td><td colspan= 8 > Total </td>"
    cabecera1 ="<td colspan= 8> Hombres</td><td colspan= 8> Mujeres</td>"
    cabecera2 = ["2017", "2016", "2015","2014","2013", "2012", "2011", "2010" ]
    
    paginaPob += cabecera
    paginaPob += cabecera1
    paginaPob += "</tr>"
    
    paginaPob += "<th>CCAA</th>"
    for i in range(3):
        for nomColumna in cabecera2:
            paginaPob+="<th>%s</th>" % (nomColumna)
        
    paginaPob+="</tr>"
    
    for provincia, anos in diccFinal.items():
        paginaPob+="<tr><td>%s</td>" % (provincia)
        for habitantesAnio in anos:
            paginaPob+="<td>%s</td>" % (habitantesAnio)
        paginaPob+="</tr>"
        
    paginaPob+="</table></p></body></html>"

    file.write(paginaPob)
    file.close()
            
    return()

