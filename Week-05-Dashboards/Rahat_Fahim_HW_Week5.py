#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
from tensorflow.keras.models import load_model
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import plotly.express as px


# In[2]:


baseball = pd.read_csv('baseball.csv')


# In[3]:


baseball


# In[4]:


baseball.count()


# In[24]:


baseball['Year'].min()


# In[19]:


baseball = baseball.dropna()


# In[20]:


avg_rnks = baseball.groupby('Team')['RankSeason'].mean().round()
avg_rnks = avg_rnks.reset_index()
teams = avg_rnks['Team']
avg_r = avg_rnks['RankSeason']


# In[21]:


fig = plt.figure(figsize = (19, 10))

plt.bar(teams, avg_r, color = 'maroon')
plt.xlabel('Teams')
plt.ylabel('RankSeason')
plt.title('Matplotlib Bar Chart Showing the Average rankseason of teams in Each league')


# In[22]:


year_list = baseball['Year'].unique().tolist()
team_list = baseball['Team'].unique().tolist()
W_list = baseball['W'].unique().tolist()
rnks_list = baseball['RankSeason'].unique().tolist()


# In[25]:


with st.sidebar:
       st.write("Select a range on the slider (it represents years)        to view a certain interval between two years ")
    #create a slider to hold user scores
new_year = st.slider(label = "Choose a value:",
                                  min_value = 1999,
                                  max_value = 2012,
                                 value = (1999,2012))

#create a multiselect widget to display genre

new_team = st.selectbox('Choose a team',
    team_list, 0)
#create a selectbox option that holds all unique years


# In[26]:


year_info = (baseball['Year'].between(*new_year))


# In[13]:


team_info = (baseball['Team'] == new_team)


# In[39]:


col1, col2 = st.columns(2)
with col1:
    st.write("""Average wins, Grouped by league""")
    rating_count_year2 = baseball[team_info & year_info]    .groupby('Year')['RankSeason'].mean().round()
    rating_count_year2 = rating_count_year2.reset_index()
    figpx = px.line(rating_count_year2, x = 'Year', y = 'RankSeason')
    st.plotly_chart(figpx)
    
with col2:
    st.write("""#### rank of teams and their league """)
    rating_count_year = baseball[team_info & year_info]    .groupby('Year')['W'].mean().round()
    rating_count_year = rating_count_year.reset_index()
    figpx = px.line(rating_count_year, x = 'Year', y = 'W')
    st.plotly_chart(figpx)


# In[ ]:




