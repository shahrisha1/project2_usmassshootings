
# coding: utf-8

# In[4]:


#import dependencies
import pandas as pd
import numpy
# import numpy as np
import seaborn as sns
import warnings
from geopy.geocoders import Nominatim #for going from loctaion to coordinates (lan/lon)
from geopy.exc import GeocoderTimedOut
import json


# In[5]:


laws_victims_df = pd.read_csv('data.csv', encoding='latin-1')
laws_victims_df.head()


# In[7]:


state=list(laws_victims_df['state'])


# In[8]:


laws=list(laws_victims_df['laws'])


# In[9]:


victims=list(laws_victims_df['totalVictims'])


# In[10]:


laws


# In[11]:


victims

