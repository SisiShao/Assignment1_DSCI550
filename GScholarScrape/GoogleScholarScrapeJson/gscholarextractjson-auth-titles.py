#!/usr/bin/env python
# coding: utf-8

# In[16]:


import json
import csv

FPdict = dict()
PUBLdict = dict()
PUBrate = dict()

with open('gscholarout2Alvin.json', 'r') as auths:
    j = json.load(auths)
    for i in j:
        key = ''
        ele = i
        try:
            ele = json.loads(i)
            key = list(ele.keys())[0]
        except:
            key = list(ele.keys())[0]
            
        finally:
            if(ele.get(key) == "N/A"):
#                 FPdict[key] = "N/A"
#                 PUBLdict[key] = "N/A"
                continue
            tmp = list()
            tmp_year = list()
            for i in ele.get(key)[2]:
                title = i.get("bib").get('title')
                year = i.get("bib").get('pub_year')
                if (title != None):
                    tmp.append(title)
                if (year != None):
                    tmp_year.append(year)
            tmp_year.sort(key = int)
            FPdict[key] = 2022 - int(tmp_year[0])
            PUBLdict[key] = tmp
            
# for i in FPdict.keys():
#     print(i)
# # print(FPdict[i])
# for l in PUBLdict.keys():
#     print(l)
# print(len(PUBLdict[l]))

for k in PUBLdict:
    new5 = PUBLdict[k][-5:]
    PUBLdict[k] = new5

# for k in PUBLdict:
#     if PUBLdict[k] == 'N/A' or FPdict[k] == 'N/A': 
#         PUBrate[k] = 'N/A'       
#     else:
#         PUBrate[k] = "{:.2f}".format((len(PUBLdict[k]))/(FPdict[k]))


# Author: [list of 5 publications]
# This info is used to scrape publication journals from Google Scholar
print(PUBLdict)


