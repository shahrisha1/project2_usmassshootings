
# coding: utf-8

# In[8]:


#import dependencies
import pandas as pd
import numpy
# import numpy as np
import seaborn as sns
import warnings
from geopy.geocoders import Nominatim #for going from loctaion to coordinates (lan/lon)
from geopy.exc import GeocoderTimedOut
import json


# In[9]:


gun_ownsership_df = pd.read_csv('gun_ownership_state.csv', encoding='latin-1')
gun_ownsership_df.head()


# In[13]:


gun_owners_state=gun_ownsership_df.set_index('state').to_dict()


# In[18]:


gun_owners_state_dict=gun_owners_state['percentage_owning_guns']


# In[19]:


gun_owners_state_dict

