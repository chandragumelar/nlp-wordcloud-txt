#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# In[3]:


# construct the path
file_path = os.path.join('data/sherlock.txt')


# In[12]:


# read the file
with open(file_path, 'r') as file:
    # Read the first 5 lines
    line_count = 0
    for line in file:
        print(line)
        line_count += 1
        if line_count == 5:
            break


# In[11]:


# generate a wordcloud image
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure() #i plan to include multiple plots
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

