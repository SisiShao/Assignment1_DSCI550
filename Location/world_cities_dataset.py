#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', None) 
pd.set_option('display.max_colwidth',None)
import requests
import os


# In[2]:


wc = pd.read_csv("worldcities.csv")


# In[3]:


wc_list = wc.city.to_list()


# In[4]:


wclat_list = wc.lat.to_list()
wclng_list = wc.lng.to_list()


# In[5]:


bik = pd.read_csv("sisi_v2.csv")
bikCC = bik.city_country.to_list()


# In[6]:


ii_list = bik.institution_info.to_list()


# In[7]:


wc_list = [c.lower() for c in wc_list]


# In[8]:


sha = []
for p in ii_list:
    p = p.strip().lstrip("[']").rstrip("']").lower()
    p = p.split(",")
    shasha = ()
    count =0 
    for luan in p:
        luan = luan.strip().lstrip("'").rstrip("'")
        if count<1:
            if luan in wc_list:
                count+=1
                ind = wc_list.index(luan)
                shagua = (wclat_list[ind],wclng_list[ind])
                shasha=shasha+shagua
    sha.append(shasha)


# In[9]:


city = []
for p in ii_list:
    p = p.strip().lstrip("[']").rstrip("']").lower()
    p = p.split(",")
    aux =[]
    for luan in p:
        luan = luan.strip().lstrip("'").rstrip("'")
        if luan in wc_list:
            if luan not in aux:
                aux.append(luan)
    city.append(aux)       


# In[10]:


emp_list = []
for c,e in enumerate(city):
    if e ==[]:
        emp_list.append(c)


# In[11]:


emp = bik.institution_info[emp_list].to_list()


# In[12]:


bik.institution_info[emp_list]


# In[13]:


API_KEY = os.environ.get("world_cities_dataset_py_API_KEY")
base_url = "https://maps.googleapis.com/maps/api/geocode/json?"


# In[14]:


shabi = []
missing_city_compound_code = []
for missing in emp:
    count =0
    shasha = ()
    aux =[]
    missing = missing.lstrip('["').lstrip("['").rstrip('"]').rstrip("']").split(",")[3:10]
    for i in missing:
        address = i
        if count<1:
            params = {'key':API_KEY,"address":address}
            response = requests.get(base_url,params=params).json()
            try:
                lat = response['results'][0]['geometry']['location']['lat']
                lng = response['results'][0]['geometry']['location']['lng']
                shasha = shasha+(lat,lng)
                count+=1
                aux.append(response['results'][0]["plus_code"]["compound_code"])
            except:
                pass
        else:
            break
    shabi.append(shasha)
    missing_city_compound_code.append(aux)


# In[15]:


count =-1
for i in emp_list: 
    count+=1
    sha[i] = shabi[count]


# In[16]:


len( missing_city_compound_code)


# In[17]:


bik["LatLng"] = sha


# In[18]:


count2 =-1
for i in emp_list: 
    count2+=1
    city[i] = missing_city_compound_code[count2]


# In[19]:


bik["city_name"] = city


# In[20]:


bik.head()


# In[21]:


bik.to_csv("sisi_v3.csv")

