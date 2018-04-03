
# coding: utf-8

# In[26]:


#import dependencies
import pandas as pd
import numpy
# import numpy as np
import seaborn as sns
import warnings
from geopy.geocoders import Nominatim #for going from loctaion to coordinates (lan/lon)
from geopy.exc import GeocoderTimedOut
import json


# In[27]:


#reading the csv file into a dataframe 
weapons_count_df = pd.read_csv('weapons.csv', encoding='latin-1')
weapons_count_df.head()


# In[28]:


weapons_count_df=weapons_count_df.fillna(value=0)


# In[29]:


list(weapons_count_df)


# In[30]:


weapons_count_df


# In[32]:


weapons_count_dict={}

weapons_count_dict['Rifle']=weapons_count_df['rifle'].sum()
weapons_count_dict['Semi Automatic Rifle']=weapons_count_df['semi_automatic_rifle'].sum()
weapons_count_dict['Shotgun']=weapons_count_df['shotgun'].sum()
weapons_count_dict['Semi Automatic Handgun']=weapons_count_df['semi_automatic_handgun'].sum()
weapons_count_dict['Handgun']=weapons_count_df['handgun'].sum()
weapons_count_dict['Long Gun']=weapons_count_df['long_gun'].sum()


# weapons_count_df['rifle'].sum()
    

 


# In[33]:


weapons_count_dict

