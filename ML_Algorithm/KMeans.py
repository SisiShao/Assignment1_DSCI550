#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('tiger_final_dataset.csv')


# In[3]:


df_train_label=df['Correction']


# In[4]:


y = df_train_label


# In[5]:


df_train_label.fillna(0,inplace=True) 


# In[6]:


df_train_attribute=df[['GreenPct','NearBodyOfWater','Rank','Overall Score','Academic Reputation Score','Citations per Faculty','Faculty Student Ratio','tavg','tmin','tmax','prcp','snow','wdir','wspd','wpgt','pres','tsun']]


# In[7]:


df_train_attribute.fillna(0,inplace=True) 


# In[8]:


df_train_attribute = df_train_attribute.apply(pd.to_numeric, errors='coerce').fillna(0)


# In[9]:


from sklearn import preprocessing  # to normalise existing X
from sklearn.cluster import KMeans
X_Norm = preprocessing.normalize(df_train_attribute)
kmeans = KMeans(n_clusters=2, random_state=0)
y_km_cos = kmeans.fit_predict(X_Norm)
y_km_cos


# In[10]:


from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2, random_state=0)
y_km = kmeans.fit_predict(df_train_attribute)
y_km


# In[11]:


from sklearn.decomposition import PCA
pca = PCA(n_components=3)
X_pca = pca.fit_transform(df_train_attribute)


# In[12]:


import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
fig, (ax1, ax2) = plt.subplots(1, 2,dpi=150)

fig1 = ax1.scatter(X_pca[:, 0], X_pca[:, 1],c=y_km, s=15, edgecolor='none', alpha=0.5,cmap=plt.cm.get_cmap('Set1', 3))
fig2 = ax2.scatter(X_pca[:, 0], X_pca[:, 1],c=df_train_label, s=15, edgecolor='none', alpha=0.5,cmap=plt.cm.get_cmap('Accent', 3))
ax1.set_title('K-means Clustering')
legend1 = ax1.legend(*fig1.legend_elements(), loc="best", title="Classes")
ax1.add_artist(legend1)
ax2.set_title('True Labels')
legend2 = ax2.legend(*fig2.legend_elements(), loc="best", title="Classes")
ax2.add_artist(legend2)


# In[18]:


jaccard_score(y, y_km,pos_label = 0)

