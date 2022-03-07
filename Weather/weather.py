#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from meteostat import Point
import matplotlib.pyplot as plt
from datetime import datetime
from meteostat import Point, Daily


# In[2]:


bik = pd.read_csv("sisi_v3.csv",parse_dates = [5])


# In[3]:


latlng = bik["LatLng"].to_list()


# In[4]:


bik["Year"] = bik["Year"].dt.strftime("%Y %-m %-d")


# In[5]:


time_info = bik["Year"].to_list()


# In[6]:


year_list = []
month_list = []
day_list = []
for t in time_info:
    year = int(t.split(" ")[0])
    year_list.append(year)
    month = int(t.split(" ")[1])
    month_list.append(month)
    day = int(t.split(" ")[2])
    day_list.append(day)


# In[7]:


tavg,tmin,tmax,prcp,snow,wdir,wspd,wpgt,pres,tsun = [],[],[],[],[],[],[],[],[],[]


# In[8]:


for (c,i) in enumerate(latlng):
    try:
        lat = float(i.strip().lstrip("(").rstrip(")").split(",")[0])
        lng = float(i.strip().lstrip("(").rstrip(")").split(",")[1])
        pair = (lat,lng)
        location = Point(lat, lng) 
        start = datetime(year_list[c],month_list[c],day_list[c])
        end = datetime(year_list[c],month_list[c],day_list[c])
        data = Daily(location,start,end)
        data = data.fetch()
        avg = float(data["tavg"].to_string().split()[2])
        tavg.append(avg)
        min = float(data["tmin"].to_string().split()[2])
        tmin.append(min)
        max = float(data["tmax"].to_string().split()[2])
        tmax.append(max)
        prcpp = float(data["prcp"].to_string().split()[2])
        prcp.append(prcpp)
        snowp = float(data["snow"].to_string().split()[2])
        snow.append(snowp)
        wdirp = float(data["wdir"].to_string().split()[2])
        wdir.append(wdirp)
        wspdp = float(data["wspd"].to_string().split()[2])
        wspd.append(wspdp)
        wpgtp = float(data["wpgt"].to_string().split()[2])
        wpgt.append(wpgtp)
        presp = float(data["pres"].to_string().split()[2])
        pres.append(presp)
        tsunp = float(data["tsun"].to_string().split()[2])
        tsun.append(tsunp)       
    except:
        tavg.append(" ")
        tmin.append(" ")
        tmax.append(" ")
        prcp.append(" ")
        snow.append(" ")
        wdir.append(" ")
        wspd.append(" ")
        wpgt.append(" ")
        pres.append(" ")
        tsun.append(" ")


# In[9]:


bik["tavg"]=tavg
bik["tmin"]=tmin
bik["tmax"]=tmax
bik["prcp"]=prcp
bik["snow"]=snow
bik["wdir"]=wdir
bik["wspd"]=wspd
bik["wpgt"]=wpgt
bik["pres"]=pres
bik["tsun"]=tsun


# In[10]:


bik.head(100)


# In[11]:


tiger = pd.read_csv("Tiger_dataset.csv")


# In[12]:


tiger["tavg"]=tavg
tiger["tmin"]=tmin
tiger["tmax"]=tmax
tiger["prcp"]=prcp
tiger["snow"]=snow
tiger["wdir"]=wdir
tiger["wspd"]=wspd
tiger["wpgt"]=wpgt
tiger["pres"]=pres
tiger["tsun"]=tsun


# In[13]:


tiger=tiger.iloc[:,1:]


# In[14]:


tiger


# In[15]:


tiger.to_csv("sisi_v4.csv",index=False)

