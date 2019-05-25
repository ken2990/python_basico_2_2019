
# coding: utf-8

# In[5]:


'''
Juan,
Espanol : 90
Mate : 80
Sociales : 85
Ciencias: 95

1. Crear una serie
2. Promedio general
3. Nota menor
4. Materias mayores o iguales a 90
'''


# In[6]:


Juan = {'Espanol': 90, 'Texas': 80, 'Sociales': 85, 'Ciencias': 95}
notas = pd.Series(Juan, name='Notas de Juan')
notas


# In[7]:


notas.mean() #me da el promedio


# In[8]:


notas.max() #me da la nota mas alta


# In[9]:


notas.min() #me da la nota minima


# In[10]:


notas[notas>=90] #notas mayores a 90

