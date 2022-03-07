#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy
import math


# In[2]:


bikdf = pd.read_csv('Bik-AuthorFeaturesTODO.csv')
# lab size
lsdf = pd.read_csv('ResearchGateLabSize.csv')
# pbulication rate
prdf = pd.read_csv('OUT_PubRate_gscholarextractjson.csv')
publish_place = pd.read_csv('gscholarJournalOut.csv')


# In[3]:


# append all authors lab size

bikdf['Lab Size'] = bikdf['Lab Size'].astype('object')
for i in range(len(bikdf['Lab Size'])):
    bikdf.at[i, 'Lab Size'] = []

# print(type(bikdf['Lab Size']))
# print(type(bikdf.at[0, 'Lab Size']))

# bikdf['Lab Size'] = bikdf['Lab Size'].tolist()
for index, row in lsdf.iterrows():
    a = row['article']
    try:
        
        bikr = bikdf[bikdf['Title'] == a].index[0] 
        bikdf.at[bikr, 'Lab Size'].append(row['lab-size'])
#         print(bikdf.at[bikr, 'Lab Size'])
    except:
        continue

# print(bikdf['Lab Size'])


# In[4]:


# append all authors publication rate

bikdf['Publication Rate'] = bikdf['Publication Rate'].astype('object')
for l in range(len(bikdf['Publication Rate'])):
    bikdf.at[l, 'Publication Rate'] = []

# print(bikdf['Publication Rate'])
# print(type(bikdf.at[0, 'Publication Rate']))
# bikr = bikdf[bikdf['Authors'].str.contains('Rounak Nassirpour', na=False)].index[0] 
# print(bikr)

for index, row in prdf.iterrows():
    auth = row['author']
    try:
        bikr = bikdf[bikdf['Authors'].str.contains(auth, na=False)].index[0] 
        bikdf.at[bikr, 'Publication Rate'].append(row['Publication Rate'])
        
    except Exception as e:
#         print(e)
        continue

# print(bikdf.at[0, 'Publication Rate'])
print(bikdf['Publication Rate'])


# In[8]:


pp = dict()  # make sure indexes pair with number of rows
for index, row in publish_place.iterrows():
    if isinstance(row['publish_place'], float):
        continue
        
    if row['author'] not in pp:
        pp[row['author']] = [row['publish_place']]
    pp[row['author']].append(row['publish_place'])

bikdf['Other Journals Published In'] = bikdf['Other Journals Published In'].astype('object')
for l in range(len(bikdf['Other Journals Published In'])):
    bikdf.at[l, 'Other Journals Published In'] = []

check = []
for index, row in bikdf.iterrows():
    auths = row['Authors']
    print(auths)
    try:
        for auth in pp.keys():
            if auth in auths:
                bikdf.at[index, 'Other Journals Published In'].append(set(pp[auth]))
            
#             bikr = bikdf[bikdf['Authors'].str.contains(auth, na=False)].index[0]
#             check.append(bikr)
#             bikdf.at[, 'Other Journals Published In'].append(set(pp[auth]))
        
    except Exception as e:
        print(e)
        continue
# print(check)


# In[9]:



print(bikdf.at[2, 'Other Journals Published In'])
print(bikdf['Other Journals Published In'])


# In[10]:


bikdf


# In[11]:


bikdf.to_csv('bik_w_author_features.csv')


# In[12]:


bikdf.to_csv('bik_w_author_features.tsv', sep="\t")


# In[ ]:




