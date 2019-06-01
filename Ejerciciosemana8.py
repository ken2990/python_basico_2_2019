
# coding: utf-8

# In[1]:


#crear un archivo csv


# In[4]:


#Crear un dataframe con nombres de columnas, "producto" "precios".


# In[5]:


import pandas as pd


# In[6]:


import numpy as np


# In[10]:


names = ['productos', 'precios']
pd.read_csv('Compras.csv', names=names)


# In[11]:


pd.read_csv('Compras.csv', header=None)
pd.read_csv('Compras.csv', names=['frutas','precio'])


# In[12]:


#Calcular el total y el precio promedio


# In[17]:


df = pd.read_csv('Compras.csv', names=['frutas','precio'])



# In[14]:





# In[19]:


df['precio'].sum()


# In[20]:


df['precio'].mean()

