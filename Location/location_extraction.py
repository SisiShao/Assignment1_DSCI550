#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pd.set_option('display.max_rows', 500)

pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', None) 
pd.set_option('display.max_colwidth',None)


# In[3]:


sis = pd.read_csv("sisi_v1.csv")


# In[4]:


sis["Year"]


# In[5]:


ins_info_list = sis.institution_info.to_list()


# In[6]:


len(ins_info_list)


# In[9]:



forbid =["research",'institute','laboratory','centre',         'school','department','departments','university','faculty','team','univ',         "-university","sciences",'discipline',        "surgery","college","hospital",'biology','departments',        "program","section","division","institut","pharmacy",        "departamento","laboratoire",'microbiology','institutes',        'national']
forbid =set(forbid)


# In[10]:


location_info=[]
for i in range(len(ins_info_list)):
    if ins_info_list[i].startswith('['):
        paper = ins_info_list[i].lstrip('[').rstrip(']').split(',')
        cc = []
        for i in paper:
            aux =set(i.lower().strip().lstrip("'").split(" "))
            if aux.isdisjoint(forbid) and (aux.intersection(forbid) == set()):
                cc.append(i)
        location = set(cc)
        location_info.append(list(location))
    else:
        paper = ins_info_list[i].strip().split(',')
        location_info.append(paper[-2:])


# In[11]:


sis["city_country"] = location_info


# In[12]:


sis = sis.iloc[: , 1:]


# In[13]:


sis.head()


# In[14]:


sis.to_csv("sisi_v2.csv",index=False)

