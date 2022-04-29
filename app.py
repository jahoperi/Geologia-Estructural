# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:13:50 2022

@author: jahop_fz60h0
"""

import streamlit as st
from streamlit_option_menu import option_menu
#from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import streamlit.components.v1 as components
import requests  # pip install requests
import plotly.express as px

import pandas as pd
#import numpy as np

#import plotly.graph_objects as go 


from PIL import Image

image = Image.open('pemex.png')
st.image(image)


    
st.title("Geología Estructural")
page_names = ['Ariel Ramírez Díaz', 'Arnulfo Zarate Santiago', 'Daniel Gómez Ochoa', 'Gustavo Gutiérrez Rodríguez', 'Jesica Aguirre Olguin', 'Jesús Alejandro García Cantú', 'José Luis Landa Mondragon', 'María Elena Arenas Martínez', 'Marybeth Garrido Hernández', 'Mónica Rodríguez Otero', 'Nestor Daniel Ortíz Najera', 'Oscar Emmanuel Guadalupe Vences Estudillo', 'Raúl Arturo Palacios Zamora', 'Rosalía Molina Mandujano', 'Uriel Román Manjarrez Juárez', 'Uzziel Saldaña Hernández', 'Verónica Iveth Ramírez Soria', 'Yessica Guerrero Amador', 'Unión de los gráficos']

page = st.radio('Navegación', page_names, index = 0)
#st.write("**La variable 'page' returns:**", page)

data = pd.read_csv("NDR.csv")
data = data.set_index('PROFESIONISTAS')

#col1, col2, col3 = st.columns(3)

col1, col2 = st.columns([100, 100])

col1.subheader("DATOS")
col1.write(data)


#1 vertical menu

#selected = option_menu(
#    menu_title = "Geología Estructural", #required
#    options = ["Ariel Ramírez Díaz", "Arnulfo Zarate Santiago", "Daniel Gómez Ochoa", "Gustavo Gutiérrez Rodríguez", "Jesica Aguirre Olguin", "Jesús Alejandro García Cantú", "José Luis Landa Mondragon", "María Elena Arenas Martínez", "Marybeth Garrido Hernández", "Mónica Rodríguez Otero", "Nestor Daniel Ortíz Najera", "Oscar Emmanuel Guadalupe Vences Estudillo", "Raúl Arturo Palacios Zamora", "Rosalía Molina Mandujano", "Uriel Román Manjarrez Juárez", "Uzziel Saldaña Hernández", "Verónica Iveth Ramírez Soria", "Yessica Guerrero Amador"], #required
#    #icons = ["house", "envelope", "envelope",  "envelope",  "envelope",  "envelope",  "envelope",  "envelope",  "envelope",  "envelope",  "envelope",  "envelope", "envelope", "envelope", "envelope", "envelope", "envelope", "envelope", "envelope",], #optional
#    #icons = ["house"],
#    menu_icon = "cast", #optional
#    default_index = 0, #optional
    
#    ) 
                    
if page == 'Ariel Ramírez Díaz':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,3,2,3,2,1,1,3,2,2,1,2,2,1,2,2,1,1,2])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Ariel Ramírez Díaz', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()
else:   
   st.subheader("")
   st.write("")
   
if page == 'Arnulfo Zarate Santiago':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,1,3,2,3,2,1,2,2,2,1,2,2,1,1,1,2,1,1,3])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Arnulfo Zarate Santiago', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show() 
else: 
    st.subheader("")
    st.write("")

if page == 'Daniel Gómez Ochoa':
     #st.title(f"Has seleccionado {selected}")
     fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,3,1,1,2,3,1,1,3,3,2,1,2,1,2,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Daniel Gómez Ochoa', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     st.plotly_chart(fig)
     #fig.show() 
else:   
    st.subheader("")
    st.write("")

if page == 'Gustavo Gutiérrez Rodríguez':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[2,1,1,1,2,2,1,1,2,1,1,1,2,1,1,1,1,1,1,1])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Gustavo Gutiérrez Rodríguez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()    
else:
    st.subheader("")
    st.write("")

if page == 'Jesica Aguirre Olguin':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,1,3,1,3,2,1,1,2,1,1,1,2,1,1,1,1,1,1,1])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Jesica Aguirre Olguin', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()    
else:
    st.subheader("")
    st.write("")

if page == 'Jesús Alejandro García Cantú':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,1,2,1,3,3,2,2,2,2,1,1,2,1,1,3,1,1,1,2])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Jesús Alejandro García Cantú', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()  
else:      
    st.subheader("")
    st.write("")  
      
if page == 'José Luis Landa Mondragon':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[2,3,4,3,3,3,2,2,3,3,3,3,4,2,2,2,2,2,2,4])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='José Luis Landa Mondragon', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()  
else:
   st.subheader("")
   st.write("")

if page == 'María Elena Arenas Martínez':
   #st.title(f"Has seleccionado {selected}")
   fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,1,2,2,2,2,1,2,3,2,1,1,2,1,1,1,1,1,1,1])
   fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='María Elena Arenas Martínez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
   fig.update_yaxes(range = [0,5])
   st.plotly_chart(fig)
   #fig.show()  
else:
    st.subheader("")
    st.write("")

if page == 'Marybeth Garrido Hernández':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[2,1,1,2,1,2,1,1,2,2,1,1,1,1,1,1,1,1,2,2])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Marybeth Garrido Hernández', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()  
else:
    st.subheader("")
    st.write("")
    
if page == 'Mónica Rodríguez Otero':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,1,3,3,3,2,2,2,3,2,1,1,3,2,2,2,2,1,2,3])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Mónica Rodríguez Otero', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()      
else:
    st.subheader("")
    st.write("")

if page == 'Nestor Daniel Ortíz Najera':
     #st.title(f"Has seleccionado {selected}")
     fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,4,2,3,2,2,2,3,2,2,2,3,3,2,3,2,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Nestor Daniel Ortíz Najera', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     st.plotly_chart(fig)
     #fig.show()  
else:
    st.subheader("")
    st.write("")

if page == 'Oscar Emmanuel Guadalupe Vences Estudillo':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,1,3,1,3,2,1,1,3,2,3,1,2,2,1,1,1,1,2,2])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Oscar Emmanuel Guadalupe Vences Estudillo', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()      
else:
     st.subheader("")
     st.write("")
    
if page == 'Raúl Arturo Palacios Zamora':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,2,2,1,2,1,2,2,2,2,1,1,1,1,3,2,1,1,2])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Raúl Arturo Palacios Zamora', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()    
else:
    st.subheader("")
    st.write("")

if page == 'Rosalía Molina Mandujano':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,1,2,2,1,1,1,1,2,1,3,3,3,2,1,1,1,1,1,2])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Rosalía Molina Mandujano', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()     
else:
    st.subheader("")
    st.write("")


if page == 'Uriel Román Manjarrez Juárez':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,1,3,1,3,2,1,3,2,1,2,1,2,1,1,2,2,1,1,2])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Uriel Román Manjarrez Juárez', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()     
else:
    st.subheader("")
    st.write("")

if page == 'Uzziel Saldaña Hernández':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,3,3,4,3,2,3,3,3,4,2,3,2,2,2,1,2,2,3])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Uzziel Saldaña Hernández', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()    
else:
    st.subheader("")
    st.write("")

if page == 'Verónica Iveth Ramírez Soria':
      #st.title(f"Has seleccionado {selected}")
      fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,1,3,2,2,2,2,2,2,2,2,1,2,2,1,2,1,1,2,2])
      fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Verónica Iveth Ramírez Soria', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
      fig.update_yaxes(range = [0,5])
      st.plotly_chart(fig)
      #fig.show()         
else:
     st.subheader("")
     st.write("")
    
if page == 'Yessica Guerrero Amador':
     #st.title(f"Has seleccionado {selected}")
     fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,3,2,2,3,2,2,1,3,1,1,1,2,1,2,2,2,2,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', title='Yessica Guerrero Amador', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     st.plotly_chart(fig)
     #fig.show()     
else:
    st.subheader("")
    st.write("")
    
if page == 'Unión de los gráficos':
     fig = px.line(x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,3,2,3,2,1,1,3,2,2,1,2,2,1,2,2,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     #fig.update_traces(name='Ariel Ramírez Díaz')

     
     fig.add_scatter(name = 'Ariel Ramírez Díaz', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,3,2,3,2,1,1,3,2,2,1,2,2,1,2,2,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=15, color="black"))
     fig.update_yaxes(range = [0,5])
     #fig.update_traces(name='Ariel Ramírez Díaz')
     #fig.update_traces(name='Arnulfo Zarate Santiago')
     #fig.update_traces(name='Daniel Gómez Ochoa')
     #fig.update_traces(name='Gustavo Gutiérrez Rodríguez')
     #fig.update_traces(name='Jesica Aguirre Olguin')
     #fig.update_traces(name='Jesús Alejandro García Cantú')
     #fig.update_traces(name='José Luis Landa Mondragon')
     #fig.update_traces(name='María Elena Arenas Martíez')
     #fig.update_traces(name='Marybeth Garrido Hernández')
     #fig.update_traces(name='Mónica Rodríguez Otero')
     #fig.update_traces(name='Nestor Daniel Ortíz Najera')
     #fig.update_traces(name='Oscar Emmanuel Guadalupe Vences Estudillo')
     #fig.update_traces(name='Raúl Arturo Palacios Zamora')
     #fig.update_traces(name='Rosalía Molina Mandujano')
     #fig.update_traces(name='Uriel Román Manjarrez Juárez')
     #fig.update_traces(name='Uzziel Saldaña Hernández')
     #fig.update_traces(name='Verónica Iveth Ramírez Soria')
     #fig.update_traces(name='Yessica Guerrero Amador')
     fig.add_scatter(name = 'Arnulfo Zarate Santiago', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,1,3,2,3,2,1,2,2,2,1,2,2,1,1,1,2,1,1,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     #fig.update_traces(name='Arnulfo Zarate Santiago')
     
     fig.add_scatter(name = 'Daniel Gómez Ochoa', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[4,3,1,1,2,3,1,1,3,3,2,1,2,1,2,2,2,2,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     #fig.update_traces(name='Daniel Gómez Ochoa')
     
     fig.add_scatter(name = 'Gustavo Gutiérrez Rodríguez', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[2,1,1,1,2,2,1,1,2,1,1,1,2,1,1,1,1,1,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     #fig.update_traces(name='Gustavo Gutiérrez Rodríguez')
     
     fig.add_scatter(name = 'Jesica Aguirre Olguin', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,1,3,1,3,2,1,1,2,1,1,1,2,1,1,1,1,1,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     #fig.update_traces(name='Jesica Aguirre Olguin')
     
     fig.add_scatter(name = 'Jesús Alejandro García Cantú', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,1,2,1,3,3,2,2,2,2,1,1,2,1,1,3,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     #fig.update_traces(name='Jesús Alejandro García Cantú')
     
     fig.add_scatter(name = 'José Luis Landa Mondragon', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[2,3,4,3,3,3,2,2,3,3,3,3,4,2,2,2,2,2,2,4])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     #fig.update_traces(name='José Luis Landa Mondragon')
     
     fig.add_scatter(name = 'María Elena Arenas Martínez', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,1,2,2,2,2,1,2,3,2,1,1,2,1,1,1,1,1,1,1])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     #fig.update_traces(name='María Elena Arenas Martíez')
     
     fig.add_scatter(name = 'Marybeth Garrido Hernández', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[2,1,1,2,1,2,1,1,2,2,1,1,1,1,1,1,1,1,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     #fig.update_traces(name='Marybeth Garrido Hernández')
     
     fig.add_scatter(name = 'Mónica Rodríguez Otero', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,1,3,3,3,2,2,2,3,2,1,1,3,2,2,2,2,1,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     #fig.update_traces(name='Mónica Rodríguez Otero')
    
     fig.add_scatter(name = 'Nestor Daniel Ortíz Najera', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,4,2,3,2,2,2,3,2,2,2,3,3,2,3,2,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     #fig.update_traces(name='Nestor Daniel Ortíz Najera')
     
     fig.add_scatter(name = 'Oscar Emmanuel Guadalupe Vences Estudillo', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,1,3,1,3,2,1,1,3,2,3,1,2,2,1,1,1,1,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     #fig.update_traces(name='Oscar Emmanuel Guadalupe Vences Estudillo')
     
     fig.add_scatter(name = 'Raúl Arturo Palacios Zamora', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,2,2,1,2,1,2,2,2,2,1,1,1,1,3,2,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     #fig.update_traces(name='Raúl Arturo Palacios Zamora')
     
     fig.add_scatter(name = 'Rosalía Molina Mandujano', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,1,2,2,1,1,1,1,2,1,3,3,3,2,1,1,1,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     #fig.update_traces(name='Rosalía Molina Mandujano')
     
     fig.add_scatter(name = 'Uriel Román Manjarrez Juárez', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,1,3,1,3,2,1,3,2,1,2,1,2,1,1,2,2,1,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     #fig.update_traces(name='Uriel Román Manjarrez Juárez')
     
     fig.add_scatter(name = 'Uzziel Saldaña Hernández', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,2,3,3,4,3,2,3,3,3,4,2,3,2,2,2,1,2,2,3])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     #fig.update_traces(name='Uzziel Saldaña Hernández')
     
     fig.add_scatter(name = 'Verónica Iveth Ramírez Soria', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,1,3,2,2,2,2,2,2,2,2,1,2,2,1,2,1,1,2,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     #fig.update_traces(name='Verónica Iveth Ramírez Soria')
     
     fig.add_scatter(name = 'Yessica Guerrero Amador', x=["Mapeo-correlaciones estratigráficas y estructurales",	"Análisis de yacimientos fracturados", "Geología estructural y restauración", "Modelo geológico y mapeo de propiedades 3D", "Tectónica salina y arcilla", "Análisis de cuencas y sistemas petroleros", "Análisis de rutas de migración", "Análisis de sellos", "Exploración y análisis de plays", "Reconstrucción estructural-paleogeografía y tectónica", "Principios sísmicos", "Construcción de modelos de velocidad y conversión a profundidad", "Interpretación estructural 2D/3D", "Migración sísmica", "Análisis de fracturas usando datos petrofísicos", "Análisis de riesgo geológico", "Estimación de recursos y reservas", "Geomecánica", "Propiedades geomecánicas de rocas", "Integración de geociencias"], y=[3,3,2,2,3,2,2,1,3,1,1,1,2,1,2,2,2,2,1,2])
     fig.update_layout(yaxis_title='Nivel de dominio', xaxis_title = 'Competencias', autosize=True, height=700, width = 1900, font=dict(family="bold, monospace", size=14, color="black"))
     fig.update_yaxes(range = [0,5])
     #fig.update_traces(name='Yessica Guerrero Amador')
     st.plotly_chart(fig)
     
else:
    st.subheader("")
    
    
