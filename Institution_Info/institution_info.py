#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv

with open('Bik dataset','r') as csvin, open('Bik dataset TSV', 'w') as tsvout:
    csvin = csv.reader(csvin)
    tsvout = csv.writer(tsvout, delimiter='\t')
    for row in csvin:
        tsvout.writerow(row)


# In[2]:


import pandas as pd
tsv_df = pd.read_csv("Bik dataset TSV",delimiter='\t',parse_dates = ["Year","Month","Correction Date"])


# In[3]:


tsv_df = tsv_df.drop(['Month'], axis = 1)


# In[4]:


tsv_df["Year"]=tsv_df["Year"].dt.strftime("%m/%d/%y")


# In[5]:


tsv_df['Correction Date']=tsv_df['Correction Date'].dt.strftime("%m/%d/%y")


# In[6]:


DOI_list = tsv_df.DOI.to_list()


# In[7]:


from habanero import Crossref
from urllib.request import urlopen
import requests
import urllib.request
from bs4 import BeautifulSoup


# # The <font color='red'>mapp dictionary </font>  is obtained from <font color='red'>*Auto_API_way.ipynb*.</font> 

# In[8]:


mapp ={'10.1002/ijc.27627':'https://pubmed.ncbi.nlm.nih.gov/22573407/',
          '10.1002/ijc.27863':'https://pubmed.ncbi.nlm.nih.gov/23001755/',
         '10.1002/ijc.27730':'https://pubmed.ncbi.nlm.nih.gov/22815231/',
         '10.1002/ijc.27927':'https://pubmed.ncbi.nlm.nih.gov/23129185/',
         '10.1002/ijc.27917':'https://pubmed.ncbi.nlm.nih.gov/23114871/',
         '10.1128/IAI.00805-10':'https://pubmed.ncbi.nlm.nih.gov/21321072/',
         '10.1128/IAI.69.10.6131–6139.2001':'https://pubmed.ncbi.nlm.nih.gov/11553552/',
         '10.1128/IAI.71.3.1209–1216.2003':'https://pubmed.ncbi.nlm.nih.gov/12595434/',
         '10.1128/IAI.71.2.766–773.2003':'https://pubmed.ncbi.nlm.nih.gov/12540556/',
         '10.1128/IAI.73.3.1754–1763.2005':'https://pubmed.ncbi.nlm.nih.gov/15731076/',
         '10.1128/IAI.00206-12':'https://pubmed.ncbi.nlm.nih.gov/22615246/',
         '10.1128/IAI.00013-12':'https://pubmed.ncbi.nlm.nih.gov/22615248/',
          '10.1128/IAI.05798-11':'https://pubmed.ncbi.nlm.nih.gov/22038917/',
          '10.1128/IAI.00063-12':'https://pubmed.ncbi.nlm.nih.gov/22585967/',
          '10.1128/IAI.01165-12':'https://pubmed.ncbi.nlm.nih.gov/23357385/',
      '10.1128/IAI.00539-13':'https://pubmed.ncbi.nlm.nih.gov/23940207/',
      '10.1111/j.1365-2672.2010.04795.x':'https://pubmed.ncbi.nlm.nih.gov/20636343/',
      '10.1111/j.1462-2920.2008.01842.x':'https://pubmed.ncbi.nlm.nih.gov/19170727/',
      '10.1111/j.1462-2920.2012.02741.x':'https://pubmed.ncbi.nlm.nih.gov/22498339/',
       '10.1111/j.1462-2920.2012.02788.x':'https://pubmed.ncbi.nlm.nih.gov/22640257/',
       '10.1111/j.1348-0421.2010.00241.x':'https://pubmed.ncbi.nlm.nih.gov/20840156/',
       '10.1111/j.1472-765X.2012.03263.x':'https://pubmed.ncbi.nlm.nih.gov/22563695/',
       '10.1186/1471-2180-10-53':'https://pubmed.ncbi.nlm.nih.gov/20167112/',
       '10.1186/1471-2180-13-113':'https://pubmed.ncbi.nlm.nih.gov/23701827/',
       '10.1186/gb-2013-14-10-r121':'https://pubmed.ncbi.nlm.nih.gov/24176123/',
       '10.1186/bcr3128':'https://pubmed.ncbi.nlm.nih.gov/22353783/',
       '10.1186/bcr3201':'https://pubmed.ncbi.nlm.nih.gov/22632416/',
       '10.1186/bcr3322':'https://pubmed.ncbi.nlm.nih.gov/22995475/',
       '10.1186/bcr3200':'https://pubmed.ncbi.nlm.nih.gov/22621393/',
       '10.1186/bcr3441':'https://pubmed.ncbi.nlm.nih.gov/23786849/',
       '10.1186/bcr3692':'https://pubmed.ncbi.nlm.nih.gov/25022892/',
       '10.1016/S0169-5002(01)00212-4':'https://pubmed.ncbi.nlm.nih.gov/11557119/',
       '10.1016/S0169-5002(03)00239-3':'https://pubmed.ncbi.nlm.nih.gov/12928127/',
       '10.1016/j.lungcan.2006.06.001':'https://pubmed.ncbi.nlm.nih.gov/16842883/',
       '10.1016/j.lungcan.2006.06.006':'https://pubmed.ncbi.nlm.nih.gov/16860902/',
       '10.1016/j.lungcan.2008.05.026':'https://pubmed.ncbi.nlm.nih.gov/18619705/',
       '10.1016/j.lungcan.2009.06.013':'https://pubmed.ncbi.nlm.nih.gov/19615783/',
       '10.1016/j.lungcan.2009.10.010':'https://pubmed.ncbi.nlm.nih.gov/19914733/',
       '10.1016/j.lungcan.2011.01.012':'https://pubmed.ncbi.nlm.nih.gov/21333374/',
       '10.1016/j.lungcan.2011.10.002':'https://pubmed.ncbi.nlm.nih.gov/22047961/',
       '10.1016/j.jaut.2005.09.016':'https://pubmed.ncbi.nlm.nih.gov/16271292/',
       '10.1016/j.jaut.2004.10.003':'https://pubmed.ncbi.nlm.nih.gov/15725579/',
       '10.1016/j.jaut.2006.05.001':'https://pubmed.ncbi.nlm.nih.gov/16797160/',
       '10.1016/j.jaut.2007.02.007':'https://pubmed.ncbi.nlm.nih.gov/17383158/',
       '10.1016/j.jaut.2008.12.003':'https://pubmed.ncbi.nlm.nih.gov/19200691/',
       '10.1016/j.jaut.2014.02.013':'https://pubmed.ncbi.nlm.nih.gov/24662148/',
       '10.1016/j.cyto.2003.11.014':'https://pubmed.ncbi.nlm.nih.gov/15016405/',
       '10.1016/j.cyto.2004.12.015':'https://pubmed.ncbi.nlm.nih.gov/15935953/',
       '10.1016/j.cyto.2004.11.009':'https://pubmed.ncbi.nlm.nih.gov/15935952/',
       '10.1016/j.cyto.2006.07.009':'https://pubmed.ncbi.nlm.nih.gov/16949835/',
       '10.1016/j.cyto.2007.01.002':'https://pubmed.ncbi.nlm.nih.gov/17376698/',
       '10.1016/j.cyto.2006.12.003':'https://pubmed.ncbi.nlm.nih.gov/17223607/',
       '10.1016/j.cyto.2005.12.007':'https://pubmed.ncbi.nlm.nih.gov/16488623/',
       '10.1016/j.cyto.2007.04.003':'https://pubmed.ncbi.nlm.nih.gov/17540578/',
       '10.1016/j.cyto.2008.06.007':'https://pubmed.ncbi.nlm.nih.gov/18809337/',
       '10.1016/j.cyto.2008.06.003':'https://pubmed.ncbi.nlm.nih.gov/18662886/',
       '10.1016/j.cyto.2008.01.001':'https://pubmed.ncbi.nlm.nih.gov/18321765/',
       '10.1016/j.cyto.2008.02.005':'https://pubmed.ncbi.nlm.nih.gov/18362077/',
       '10.1016/j.cyto.2009.07.004':'https://pubmed.ncbi.nlm.nih.gov/19660963/',
       '10.1016/j.cyto.2008.12.021':'https://pubmed.ncbi.nlm.nih.gov/19231232/',
       '10.1016/j.cyto.2008.12.013':'https://pubmed.ncbi.nlm.nih.gov/19251437/',
       '10.1016/j.cyto.2008.12.015':'https://pubmed.ncbi.nlm.nih.gov/19223199/',
       '10.1016/j.cyto.2011.06.006':'https://pubmed.ncbi.nlm.nih.gov/21733716/',
        '10.1016/j.cyto.2011.08.017':'https://pubmed.ncbi.nlm.nih.gov/21890375/',
        '10.1016/j.cyto.2011.02.016':'https://pubmed.ncbi.nlm.nih.gov/21419645/',
       '10.1016/j.cyto.2011.06.005':'https://pubmed.ncbi.nlm.nih.gov/21742513/',
        '10.1016/j.cyto.2012.08.025':'https://pubmed.ncbi.nlm.nih.gov/23017228/',
       '10.1016/j.cyto.2013.04.009':'https://pubmed.ncbi.nlm.nih.gov/23664770/',
        '10.1016/j.cyto.2013.04.005':'https://pubmed.ncbi.nlm.nih.gov/23612013/',
        '10.1016/j.cyto.2014.07.249':'https://pubmed.ncbi.nlm.nih.gov/25127907/',
        '10.1038/34214':'https://pubmed.ncbi.nlm.nih.gov/9422513/',
    '10.1038/44188':'https://pubmed.ncbi.nlm.nih.gov/10524633/',
    '10.1038/nature07034':'https://pubmed.ncbi.nlm.nih.gov/18552838/',
       '10.1038/nature07091':'https://pubmed.ncbi.nlm.nih.gov/18594509/',
       '10.1038/nature08027':'https://pubmed.ncbi.nlm.nih.gov/19483678/',
       '10.1038/nature10539':'https://pubmed.ncbi.nlm.nih.gov/22012259/',
       '10.1038/nature12878':'https://pubmed.ncbi.nlm.nih.gov/24336215/',
       '10.1038/onc.2013.184':'https://pubmed.ncbi.nlm.nih.gov/23728342/',
       '10.1038/onc.2013.237':'https://pubmed.ncbi.nlm.nih.gov/23770856/',
       '10.1038/onc.2014.404':'https://pubmed.ncbi.nlm.nih.gov/25531324/',
       '10.1038/onc.2014.22':'https://pubmed.ncbi.nlm.nih.gov/24632608/',
       '10.3892/ijo.2012.1714':'https://pubmed.ncbi.nlm.nih.gov/23175173/',
       '10.3892/ijo.2012.1617':'https://pubmed.ncbi.nlm.nih.gov/27826623/',
       '10.3892/ijo.2012.1470':'https://pubmed.ncbi.nlm.nih.gov/22581300/',
       '10.3892/ijo.2012.1343':'https://pubmed.ncbi.nlm.nih.gov/22293778/',
       '10.3892/ijo.2013.1789':'https://pubmed.ncbi.nlm.nih.gov/23354006/',
       '10.3892/ijo.2012.1741':'https://pubmed.ncbi.nlm.nih.gov/23254774/',
       '10.3892/ijo.2013.1761':'https://pubmed.ncbi.nlm.nih.gov/23292068/',
        '10.3892/ijo.2013.1809':'https://pubmed.ncbi.nlm.nih.gov/23403907/',
       '10.3892/ijo.2013.1903':'https://pubmed.ncbi.nlm.nih.gov/23588792/',
       '10.1016/j.ccr.2013.04.019':'https://pubmed.ncbi.nlm.nih.gov/23727022/',
       '10.1016/j.ccr.2012.10.003':'https://pubmed.ncbi.nlm.nih.gov/23153534/',
       '10.1016/j.ccr.2013.12.007':'https://pubmed.ncbi.nlm.nih.gov/24434208/',
       '10.1016/j.ccr.2013.02.018':'https://pubmed.ncbi.nlm.nih.gov/23597563/',
       '10.1016/j.ccell.2014.09.008':'https://pubmed.ncbi.nlm.nih.gov/25446900/',
       '10.1073/pnas.1101273108':'https://pubmed.ncbi.nlm.nih.gov/21383157/',
       '10.1073/pnas.1108537109':'https://pubmed.ncbi.nlm.nih.gov/22451918/',
       '10.1073/pnas.1202214109':'https://pubmed.ncbi.nlm.nih.gov/22492977/',
       '10.1073/pnas.1310331110':'https://pubmed.ncbi.nlm.nih.gov/23798383/',
        '10.1073/pnas.1211179110':'https://pubmed.ncbi.nlm.nih.gov/23302695/',
       '10.1073/pnas.1319190110':'https://pubmed.ncbi.nlm.nih.gov/24367099/'
      }


# In[9]:


'10.1002/ijc.27627' in mapp.keys()


# In[10]:


institution_info = []
problem = []
for doi in DOI_list:
    if ('pone' in doi) or ('pbio' in doi) or ('pgen' in doi) or ('ppat' in doi) or ('pntd' in doi):
        url =  'https://doi.org/'+doi
        response = requests.get(url)
        soup = BeautifulSoup(response.text)
        metas = soup.find_all('meta')
        new_info = [meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'citation_author_institution']
        institution_info.append(new_info)
    elif doi in mapp.keys():
        url = mapp.get(doi)
        url_contents = urllib.request.urlopen(url).read()
        Soup = BeautifulSoup(url_contents)
        anchors = Soup.findAll('a', href=True)
        a = anchors[1]
        try:
            institution_info.append(a.attrs["title"])
        except:
            institution_info.append([])
    elif 'PMID:' in doi:
        url = 'https://pubmed.ncbi.nlm.nih.gov/'+doi.lstrip('PMID: ')
        url_contents = urllib.request.urlopen(url).read()
        Soup = BeautifulSoup(url_contents)
        anchors = Soup.findAll('a', href=True)
        a = anchors[1]
        institution_info.append(a.attrs["title"])
    
        
    else:
        cr = Crossref()
        try:
            x = cr.works(ids = doi)
            info =x['message']['author']
            aux=[]
            for i in range(len(info)):
                for j in range(len(info[i]["affiliation"])):
                    aux.append(info[i]["affiliation"][j]["name"])

            institution_info.append(aux)
        except:
            problem.append(doi)
            institution_info.append("  ")


# In[11]:


count=-1
inde =[]
for e in institution_info:
    count+=1
    if e ==[]:
        inde.append(count)


# In[12]:


emp_doi = [DOI_list[j] for j in inde]


# In[13]:


len(emp_doi)


# In[14]:


emp_doi


# In[15]:


tsv_df['institution_info']=institution_info


# In[16]:


tsv_df.institution_info


# In[17]:


tsv_df.head()


# In[18]:


tsv_df.to_csv("sisi_v1.csv",index=False)

