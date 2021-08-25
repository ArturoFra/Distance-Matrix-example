#!/usr/bin/env python
# coding: utf-8

# # Distancias

# In[1]:


from scipy.spatial import distance_matrix
import pandas as pd 
import numpy as np


# In[4]:


data = pd.read_csv("C:/Users/A Emiliano Fragoso/Desktop/MLcourse/python-ml-course-master/datasets/movies/movies.csv", sep=";")
data.head()


# In[5]:


movies = data.columns.values.tolist()[1:]


# In[6]:


movies


# In[7]:


dd1=distance_matrix(data[movies], data[movies], p=1)
dd2=distance_matrix(data[movies], data[movies], p=2)
dd10=distance_matrix(data[movies], data[movies], p=10)


# In[8]:


dd1


# In[9]:


def dm_to_df(dd, col_name):
    import pandas as pd
    return pd.DataFrame(dd, index=col_name, columns = col_name)


# In[10]:


dm_to_df(dd1, data["user_id"])


# In[12]:


dm_to_df(dd2, data["user_id"])


# In[13]:


dm_to_df(dd10, data["user_id"])


# In[15]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 


# In[19]:


fig=plt.figure()
ax=fig.add_subplot(111, projection = "3d")
ax.scatter(xs = data["star_wars"], ys= data["lord_of_the_rings"], zs= data["harry_potter"])


# In[ ]:





# In[17]:





# In[ ]:





# In[ ]:




