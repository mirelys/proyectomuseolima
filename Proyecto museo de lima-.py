#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import plotly.graph_objects as go


# In[3]:


#llama informacion http
lima=pd.read_html('http://quant.cl/places/Lima_museo')[0]


# In[4]:


#plataforma  de mapa online
mapbox_access_token ='pk.eyJ1IjoiZmFycmVkb25kbyIsImEiOiJjanc2ZnR2MjMxOW42NDFvdzJpZG5haDhiIn0.xGE3lzz9LPPcppdn03eeeQ'
MAT=mapbox_access_token


# In[5]:


#Diseño del titulo 
layout=go.Layout(title='Museos de Lima')


# In[6]:


#DataFrame de pandas ordenado
#hoverinfo='name' no muestra nombres de los museos
data=[go.Scattermapbox(lat=lima.lat,lon=lima.lng,mode='markers',text=lima.name)]


# In[7]:


#mostrar data
print(data)


# In[8]:


# construir figuras como diccionarios y listas 
fig=go.Figure(data=data, layout=layout)


# In[9]:


#método que puede usarse para actualizar varias propiedades anidadas del diseño de una figura
fig.update_layout(
hovermode='closest',
mapbox=go.layout.Mapbox(accesstoken=MAT,                
center=go.layout.mapbox.Center(lat=-12,lon=-77),zoom=10,style='light'))
             


# In[26]:


#mostrará la figura usando los renderizadores predeterminados actuales
fig.show()


# In[ ]:




