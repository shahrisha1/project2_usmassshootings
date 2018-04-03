
# coding: utf-8

# In[1]:


#import dependencies
import pandas as pd
import numpy as np
import seaborn as sns
import warnings
from geopy.geocoders import Nominatim #for going from loctaion to coordinates (lan/lon)
from geopy.exc import GeocoderTimedOut


# # Data Cleaning

# In[2]:


#reading the csv file into a dataframe 
shootings_df = pd.read_csv('usmassdata.csv', encoding='latin-1')
shootings_df.head()


# In[3]:


#testing for Geopy to retrieve (latitude , longitude) based on the "Location" field of the dataframe 
test_address = "Sutherland Springs, TX"
geolocator=Nominatim(timeout=10)

try:
    location = geolocator.geocode(test_address)
    print((location.latitude, location.longitude))
except GeocoderTimedOut as e:
    print("Error: geocode failed on input %s with message %s"%(test_address, e.message))


# In[ ]:


# # Loop through the dataframe to check if the latitude is missing. 
# # If the Latitue is a "NaN" then update the (Lat, Lon) data from Geopy
# for index, row in shootings_df.iterrows():
#         try:
#             location = geolocator.geocode(row['Location'])
#             shootings_df.loc[index, 'latitude']= location.latitude
#             shootings_df.loc[index, 'longitude']= location.longitude
#         except GeocoderTimedOut as e:
#             print("Error: geocode failed on input %s with message %s"%(row['Location'], e.message))


# In[4]:


# adding redults to another dataframe so that there is no confusion when referencing for Database creation 
complete_shootings_df = shootings_df
complete_shootings_df.head(100)      


# In[5]:


# list of all column headers
list(complete_shootings_df)


# In[6]:


#rename column headers so that there are no spaces & better usability

complete_shootings_df = complete_shootings_df.rename(columns={'Case': 'case', 
                                        'Location': 'location', 
                                        'Date': 'date', 
                                        'Year': 'year', 
                                        'Summary': 'summary', 
                                        'Fatalities': 'fatalities', 
                                        'Injured': 'injured', 
                                        'Total victims': 'total_victims', 
                                        'Venue': 'venue', 
                                        'Prior signs of mental health issues': 'prior_signs_mental_health', 
                                        'Mental health - details': 'mental_health', 
                                        'Weapons obtained legally': 'weapons_obtained_legally', 
                                        'Where obtained': 'where_obtained',
                                        'Type of weapons': 'type_weapon', 
                                        'Weapon details': 'weapon_details', 
                                        'Race': 'race', 
                                        'Gender': 'gender', 
                                        'Sources': 'sources', 
                                        'Mental Health Sources': 'mental_health_sources', 
                                        'Type': 'shooting_type'})

complete_shootings_df.head()


# In[7]:


# recheck column headers
complete_shootings_df.info()


# In[8]:


#update the new dataframe with city/state split from location
complete_shootings_df[['city', 'state']] = complete_shootings_df.location.str.split(',', expand = True)
complete_shootings_df.head()


# In[9]:


list(complete_shootings_df)


# In[10]:


complete_shootings_df.state.value_counts()


# In[11]:


# Condense all "White"
complete_shootings_df.state = complete_shootings_df.state.apply(lambda x: x.replace('CA', 'California'))
complete_shootings_df.state = complete_shootings_df.state.apply(lambda x: x.replace('PA', 'Pennsylvania'))
complete_shootings_df.state = complete_shootings_df.state.apply(lambda x: x.replace('D.C.', 'Washington D.C.'))
complete_shootings_df.state = complete_shootings_df.state.apply(lambda x: x.replace('TX', 'Texas'))
complete_shootings_df.state = complete_shootings_df.state.apply(lambda x: x.replace('LA', 'Louisiana'))
complete_shootings_df.state = complete_shootings_df.state.apply(lambda x: x.replace('WA', 'Washington'))
complete_shootings_df.state = complete_shootings_df.state.apply(lambda x: x.replace('NV', 'Nevada'))
complete_shootings_df.state = complete_shootings_df.state.apply(lambda x: x.replace('MD', 'Maryland'))
complete_shootings_df.state = complete_shootings_df.state.apply(lambda x: x.replace('CO', 'Colorado'))

# print
complete_shootings_df.state.value_counts()


# In[12]:


#clean up dataframe columns
complete_shootings_df.race.value_counts()


# In[13]:


complete_shootings_df['race'].replace(['white', 'black', 'unclear'], 
                                      ['White', 'Black', 'Unknown'], inplace=True)


complete_shootings_df.race.value_counts()


# In[14]:


complete_shootings_df.gender.value_counts()


# In[15]:


complete_shootings_df['gender'].replace(['M'], 
                                      ['Male'], inplace=True)

complete_shootings_df.gender.value_counts()


# In[16]:


complete_shootings_df.venue.value_counts()


# In[17]:


complete_shootings_df['venue'].replace(['Other\r', '\rWorkplace'], 
                                      ['Other', 'Workplace'], inplace=True)

complete_shootings_df.venue.value_counts()


# In[18]:


complete_shootings_df.prior_signs_mental_health.value_counts()


# In[19]:


complete_shootings_df['prior_signs_mental_health'].replace(['TBD','Unclear'], 
                                      ['Unknown','Unknown'], inplace=True)


complete_shootings_df.prior_signs_mental_health.value_counts()


# In[20]:


complete_shootings_df.weapons_obtained_legally.value_counts()


# In[21]:



complete_shootings_df['weapons_obtained_legally'].replace(['TBD', '\rYes', 'Yes ("some of the weapons were purchased legally and some of them may not have been")', 'Kelley passed federal criminal background checks; the US Air Force failed to provide information on his criminal history to the FBI'], 
                                      ['Unknown','Yes','Yes','Unknown'], inplace=True)


complete_shootings_df.weapons_obtained_legally.value_counts()


# In[22]:


complete_shootings_df.total_victims.value_counts()


# In[23]:


complete_shootings_df['total_victims'].replace(['758+','11 (dozens more were reportedly injured in the panic)', '46+'], 
                                      ['758','11','46'], inplace=True)


complete_shootings_df.total_victims.value_counts()


# In[24]:


complete_shootings_df.injured.value_counts()


# In[25]:


complete_shootings_df['injured'].replace(['700+'], 
                                      ['700'], inplace=True)


complete_shootings_df.injured.value_counts()


# In[26]:


for col in complete_shootings_df.columns:
    try:
        str(complete_shootings_df[col].iloc[0])
        complete_shootings_df[col] = complete_shootings_df[col].apply(lambda x: x.replace('\r', ''))
    except:
        pass


# In[28]:


# Loop through the dataframe to check if the latitude is missing. 
# If the Latitue is a "NaN" then update the (Lat, Lon) data from Geopy
for index, row in complete_shootings_df.iterrows():
        try:
            location = geolocator.geocode(row['location'])
            complete_shootings_df.loc[index, 'latitude']= location.latitude
            complete_shootings_df.loc[index, 'longitude']= location.longitude
        except GeocoderTimedOut as e:
            print("Error")
            # print("Error: geocode failed on input %s with message %s"%(row['Location'], e.message))


# In[30]:


# complete_shootings_df.race.value_counts()
complete_shootings_df.head(100)


# In[ ]:


complete_shootings_df.to_csv('clean_shooting.csv', index=False)


# In[ ]:


pd.read_csv('clean_shooting.csv')


# # Gun Law Data

# In[ ]:


# # complete_shootings_df.to_csv("clean_shooting.csv", encoding='utf-8', index = False) #, index = False)
# #reading the csv file into a dataframe 
# gun_laws_df = pd.read_csv('gunlawsbystate.csv', encoding='latin-1')
# gun_laws_df.head()


# In[ ]:


# state_law = gun_laws_df[['state','lawtotal']]
# state_law.head()


# In[ ]:


# pd.read_csv('clean_shooting.csv')


# In[31]:


# import matplotlib.pyplot as plt
# from subprocess import check_output
# from wordcloud import WordCloud, STOPWORDS
# stopwords = set(STOPWORDS)


# In[32]:


# wordcloud = WordCloud(
#                           background_color='black',
#                           stopwords=stopwords,
#                           max_words=200,
#                           max_font_size=40, 
#                          random_state=42
#                          ).generate(str(complete_shootings_df['summary']))

# plt.figure(figsize=(12,8))
# plt.imshow(wordcloud)
# plt.axis('off')
# plt.show()


# In[39]:


# import plotly.plotly as py


# # Database Creation

# In[ ]:


# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect


# In[ ]:


# Create an engine to a SQLite database file called `shootings.sqlite`
engine = create_engine("sqlite:///shootings.sqlite")


# In[ ]:


# Create a session
session = Session(engine)


# In[ ]:


# Create a connection to the engine called `conn`
conn = engine.connect()


# In[ ]:


#append data from csv created df to correct classes(tables)
complete_shootings_df.to_sql('shootings', engine, if_exists='append', index=False)


# In[ ]:


# Create the inspector and connect it to the engine
inspector = inspect(engine)
# Collect the names of tables within the database
inspector.get_table_names()


# In[ ]:


# Using the inspector to print the column names within the 'dow' table and its types
columns = inspector.get_columns('shootings')
for column in columns:
    print(column["name"], column["type"])

