#!/usr/bin/env python
# coding: utf-8

# In[12]:


import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# In[4]:


# get cwd
cwd = os.getcwd()
cwd


# In[6]:


ls


# In[8]:


# construct the path
file_path = os.path.join(cwd, 'sherlock.txt')

# read the file
with open(file_path, 'r') as file:
    text = file.read()


# In[13]:


# generate a wordcloud image
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure() #i plan to include multiple plots
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

