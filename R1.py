#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import locale
from funciones import csvtabla

def r1():
    dicc = csvtabla("entradas/poblacionProvinciasHM2010-17.csv", 1)
    
    #variacion absoulta
    diccFinal= {}
    locale.setlocale(locale.LC_ALL,'')
    for provincia in dicc:
        diccFinal[provincia]=[]
        for ano in range(7):
            diccFinal[provincia].append( float(dicc[provincia][ano]) - float(dicc[provincia][ano + 1]))
            
    #variacion relativa
    for provincia in dicc:
        for ano in range(7):
            diccFinal[provincia].append( (float(diccFinal[provincia][ano]) / float(dicc[provincia][ano + 1]))*100)
            
    #cambio de formato
    for provincia in dicc:
        for ano in range(14):
            diccFinal[provincia][ano] = locale.format_string('%.2f', diccFinal[provincia][ano], grouping=True) 
        
    
    
    fileEstilo=open("estilo.css","w", encoding="utf8")

    estilo="""  table, th, td {
                border-collapse: collapse;    
                border:1px solid black;
                font-family: Arial, Helvetica, sans-serif;
                padding: 8px;
                
            }  """

    fileEstilo.write(estilo)
    fileEstilo.close()
            
            
    file=open("resultados/variacionProvincias.html","w", encoding="utf8")
    
    paginaPob = """<!DOCTYPE html><html>
    <head><title>Población</title>
    <link rel="stylesheet" href="estilo.css">
    <meta charset="utf8"></head>
    <body><h1>Variación de población entre 2011-2017</h1>"""
    
    paginaPob+= """<p><table>
    <tr>"""
    cabecera = "<td colspan = 1> </td><td colspan= 7 > Variacion absoluta </td>"
    cabecera1 ="<td colspan= 7 > Variacion relativa </td>"
    cabecera2 = ["Provincia", "2017", "2016", "2015","2014","2013", "2012", "2011", "2017", "2016", "2015","2014","2013", "2012", "2011"  ]
    paginaPob += cabecera
    paginaPob += cabecera1
    paginaPob += "</tr>"
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
