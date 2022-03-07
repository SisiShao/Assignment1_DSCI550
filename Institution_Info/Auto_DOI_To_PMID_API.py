#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlopen
import requests
import urllib.request
from bs4 import BeautifulSoup


# In[27]:


emp = ['10.1002/ijc.27627',
 '10.1002/ijc.27863',
 '10.1002/ijc.27730',
 '10.1002/ijc.27927',
 '10.1002/ijc.27917',
 '10.1128/IAI.00805-10',
 '10.1128/IAI.69.10.6131–6139.2001',
 '10.1128/IAI.71.3.1209–1216.2003',
 '10.1128/IAI.71.2.766–773.2003',
 '10.1128/IAI.73.3.1754–1763.2005',
 '10.1128/IAI.00206-12',
 '10.1128/IAI.00013-12',
 '10.1128/IAI.05798-11',
 '10.1128/IAI.00063-12',
 '10.1128/IAI.01165-12',
 '10.1128/IAI.00539-13',
 '10.1111/j.1365-2672.2010.04795.x',
 '10.1111/j.1462-2920.2008.01842.x',
 '10.1111/j.1462-2920.2012.02741.x',
 '10.1111/j.1462-2920.2012.02788.x',
 '10.1111/j.1348-0421.2010.00241.x',
 '10.1111/j.1472-765X.2012.03263.x',
 '10.1186/1471-2180-10-53',
 '10.1186/1471-2180-13-113',
 '10.1186/gb-2013-14-10-r121',
 '10.1186/bcr3128',
 '10.1186/bcr3201',
 '10.1186/bcr3322',
 '10.1186/bcr3200',
 '10.1186/bcr3441',
 '10.1186/bcr3692',
 '10.1016/S0169-5002(01)00212-4',
 '10.1016/S0169-5002(03)00239-3',
 '10.1016/j.lungcan.2006.06.001',
 '10.1016/j.lungcan.2006.06.006',
 '10.1016/j.lungcan.2008.05.026',
 '10.1016/j.lungcan.2009.06.013',
 '10.1016/j.lungcan.2009.10.010',
 '10.1016/j.lungcan.2011.01.012',
 '10.1016/j.lungcan.2011.10.002',
 '10.1016/j.jaut.2005.09.016',
 '10.1016/j.jaut.2004.10.003',
 '10.1016/j.jaut.2006.05.001',
 '10.1016/j.jaut.2007.02.007',
 '10.1016/j.jaut.2008.12.003',
 '10.1016/j.jaut.2014.02.013',
 '10.1016/j.cyto.2003.11.014',
 '10.1016/j.cyto.2004.12.015',
 '10.1016/j.cyto.2004.11.009',
 '10.1016/j.cyto.2006.07.009',
 '10.1016/j.cyto.2007.01.002',
 '10.1016/j.cyto.2006.12.003',
 '10.1016/j.cyto.2005.12.007',
 '10.1016/j.cyto.2007.04.003',
 '10.1016/j.cyto.2008.06.007',
 '10.1016/j.cyto.2008.06.003',
 '10.1016/j.cyto.2008.01.001',
 '10.1016/j.cyto.2008.02.005',
 '10.1016/j.cyto.2009.07.004',
 '10.1016/j.cyto.2008.12.021',
 '10.1016/j.cyto.2008.12.013',
 '10.1016/j.cyto.2008.12.015',
 '10.1016/j.cyto.2011.06.006',
 '10.1016/j.cyto.2011.08.017',
 '10.1016/j.cyto.2011.02.016',
 '10.1016/j.cyto.2011.06.005',
 '10.1016/j.cyto.2012.08.025',
 '10.1016/j.cyto.2013.04.009',
 '10.1016/j.cyto.2013.04.005',
 '10.1016/j.cyto.2014.07.249',
 '10.1038/34214',
 '10.1038/44188',
 '10.1038/nature07034',
 '10.1038/nature07091',
 '10.1038/nature08027',
 '10.1038/nature10539',
 '10.1038/nature12878',
 '10.1038/onc.2013.184',
 '10.1038/onc.2013.237',
 '10.1038/onc.2014.404',
 '10.1038/onc.2014.22',
 '10.3892/ijo.2012.1714',
 '10.3892/ijo.2012.1617',
 '10.3892/ijo.2012.1470',
 '10.3892/ijo.2012.1343',
 '10.3892/ijo.2013.1789',
 '10.3892/ijo.2012.1741',
 '10.3892/ijo.2013.1761',
 '10.3892/ijo.2013.1809',
 '10.3892/ijo.2013.1903',
 '10.1016/j.ccr.2013.04.019',
 '10.1016/j.ccr.2012.10.003',
 '10.1016/j.ccr.2013.12.007',
 '10.1016/j.ccr.2013.02.018',
 '10.1016/j.ccell.2014.09.008',
 '10.1073/pnas.1101273108',
 '10.1073/pnas.1108537109',
 '10.1073/pnas.1202214109',
 '10.1073/pnas.1310331110',
 '10.1073/pnas.1211179110',
 '10.1073/pnas.1319190110']


# In[93]:


mapp = {}
missing =[]


# In[86]:


emp[6]


# In[94]:


for doi in emp:
    url = ("https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids="+doi).replace(u"\u2013", "-")
    r = urlopen(url).read().decode()
    try:
        mapp[doi] = "https://pubmed.ncbi.nlm.nih.gov/"+        r.split("doi")[2].split('pmid="')[1].split(' ')[0].rstrip('"')+"/"
    except:
        missing.append(doi)


# In[97]:


len(mapp)


# In[112]:


missing


# In[108]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# In[111]:


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.pmid2cite.com/doi-to-pmid-converter")
'''
The "https://www.pmid2cite.com/doi-to-pmid-converter" will block you if too many requests are made at the same time.
Will need to contact them for batch processing on your ip.
You can choose one and only one DOI to test the below code if you cannot contact them. 

'''
for m in missing: 
    try:
        button = driver.find_element_by_xpath('//input[@placeholder="Please enter DOI"]').send_keys(m)
        button2 = driver.find_element_by_xpath('//button').click()
        result = driver.find_elements_by_xpath('//a[@target="_blank"]')
        for r in result:
            if r.text != '':
                mapp[e] = r.text.strip()
    except:
        mapp[e] = 'NA'


# ## If you have contacted "https://www.pmid2cite.com/doi-to-pmid-converter" to ask for batch processing permission, the resulting mapp dictionary will look as follow:

# mapp ={'10.1002/ijc.27627':'https://pubmed.ncbi.nlm.nih.gov/22573407/',
#           '10.1002/ijc.27863':'https://pubmed.ncbi.nlm.nih.gov/23001755/',
#          '10.1002/ijc.27730':'https://pubmed.ncbi.nlm.nih.gov/22815231/',
#          '10.1002/ijc.27927':'https://pubmed.ncbi.nlm.nih.gov/23129185/',
#          '10.1002/ijc.27917':'https://pubmed.ncbi.nlm.nih.gov/23114871/',
#          '10.1128/IAI.00805-10':'https://pubmed.ncbi.nlm.nih.gov/21321072/',
#          '10.1128/IAI.69.10.6131–6139.2001':'https://pubmed.ncbi.nlm.nih.gov/11553552/',
#          '10.1128/IAI.71.3.1209–1216.2003':'https://pubmed.ncbi.nlm.nih.gov/12595434/',
#          '10.1128/IAI.71.2.766–773.2003':'https://pubmed.ncbi.nlm.nih.gov/12540556/',
#          '10.1128/IAI.73.3.1754–1763.2005':'https://pubmed.ncbi.nlm.nih.gov/15731076/',
#          '10.1128/IAI.00206-12':'https://pubmed.ncbi.nlm.nih.gov/22615246/',
#          '10.1128/IAI.00013-12':'https://pubmed.ncbi.nlm.nih.gov/22615248/',
#           '10.1128/IAI.05798-11':'https://pubmed.ncbi.nlm.nih.gov/22038917/',
#           '10.1128/IAI.00063-12':'https://pubmed.ncbi.nlm.nih.gov/22585967/',
#           '10.1128/IAI.01165-12':'https://pubmed.ncbi.nlm.nih.gov/23357385/',
#       '10.1128/IAI.00539-13':'https://pubmed.ncbi.nlm.nih.gov/23940207/',
#       '10.1111/j.1365-2672.2010.04795.x':'https://pubmed.ncbi.nlm.nih.gov/20636343/',
#       '10.1111/j.1462-2920.2008.01842.x':'https://pubmed.ncbi.nlm.nih.gov/19170727/',
#       '10.1111/j.1462-2920.2012.02741.x':'https://pubmed.ncbi.nlm.nih.gov/22498339/',
#        '10.1111/j.1462-2920.2012.02788.x':'https://pubmed.ncbi.nlm.nih.gov/22640257/',
#        '10.1111/j.1348-0421.2010.00241.x':'https://pubmed.ncbi.nlm.nih.gov/20840156/',
#        '10.1111/j.1472-765X.2012.03263.x':'https://pubmed.ncbi.nlm.nih.gov/22563695/',
#        '10.1186/1471-2180-10-53':'https://pubmed.ncbi.nlm.nih.gov/20167112/',
#        '10.1186/1471-2180-13-113':'https://pubmed.ncbi.nlm.nih.gov/23701827/',
#        '10.1186/gb-2013-14-10-r121':'https://pubmed.ncbi.nlm.nih.gov/24176123/',
#        '10.1186/bcr3128':'https://pubmed.ncbi.nlm.nih.gov/22353783/',
#        '10.1186/bcr3201':'https://pubmed.ncbi.nlm.nih.gov/22632416/',
#        '10.1186/bcr3322':'https://pubmed.ncbi.nlm.nih.gov/22995475/',
#        '10.1186/bcr3200':'https://pubmed.ncbi.nlm.nih.gov/22621393/',
#        '10.1186/bcr3441':'https://pubmed.ncbi.nlm.nih.gov/23786849/',
#        '10.1186/bcr3692':'https://pubmed.ncbi.nlm.nih.gov/25022892/',
#        '10.1016/S0169-5002(01)00212-4':'https://pubmed.ncbi.nlm.nih.gov/11557119/',
#        '10.1016/S0169-5002(03)00239-3':'https://pubmed.ncbi.nlm.nih.gov/12928127/',
#        '10.1016/j.lungcan.2006.06.001':'https://pubmed.ncbi.nlm.nih.gov/16842883/',
#        '10.1016/j.lungcan.2006.06.006':'https://pubmed.ncbi.nlm.nih.gov/16860902/',
#        '10.1016/j.lungcan.2008.05.026':'https://pubmed.ncbi.nlm.nih.gov/18619705/',
#        '10.1016/j.lungcan.2009.06.013':'https://pubmed.ncbi.nlm.nih.gov/19615783/',
#        '10.1016/j.lungcan.2009.10.010':'https://pubmed.ncbi.nlm.nih.gov/19914733/',
#        '10.1016/j.lungcan.2011.01.012':'https://pubmed.ncbi.nlm.nih.gov/21333374/',
#        '10.1016/j.lungcan.2011.10.002':'https://pubmed.ncbi.nlm.nih.gov/22047961/',
#        '10.1016/j.jaut.2005.09.016':'https://pubmed.ncbi.nlm.nih.gov/16271292/',
#        '10.1016/j.jaut.2004.10.003':'https://pubmed.ncbi.nlm.nih.gov/15725579/',
#        '10.1016/j.jaut.2006.05.001':'https://pubmed.ncbi.nlm.nih.gov/16797160/',
#        '10.1016/j.jaut.2007.02.007':'https://pubmed.ncbi.nlm.nih.gov/17383158/',
#        '10.1016/j.jaut.2008.12.003':'https://pubmed.ncbi.nlm.nih.gov/19200691/',
#        '10.1016/j.jaut.2014.02.013':'https://pubmed.ncbi.nlm.nih.gov/24662148/',
#        '10.1016/j.cyto.2003.11.014':'https://pubmed.ncbi.nlm.nih.gov/15016405/',
#        '10.1016/j.cyto.2004.12.015':'https://pubmed.ncbi.nlm.nih.gov/15935953/',
#        '10.1016/j.cyto.2004.11.009':'https://pubmed.ncbi.nlm.nih.gov/15935952/',
#        '10.1016/j.cyto.2006.07.009':'https://pubmed.ncbi.nlm.nih.gov/16949835/',
#        '10.1016/j.cyto.2007.01.002':'https://pubmed.ncbi.nlm.nih.gov/17376698/',
#        '10.1016/j.cyto.2006.12.003':'https://pubmed.ncbi.nlm.nih.gov/17223607/',
#        '10.1016/j.cyto.2005.12.007':'https://pubmed.ncbi.nlm.nih.gov/16488623/',
#        '10.1016/j.cyto.2007.04.003':'https://pubmed.ncbi.nlm.nih.gov/17540578/',
#        '10.1016/j.cyto.2008.06.007':'https://pubmed.ncbi.nlm.nih.gov/18809337/',
#        '10.1016/j.cyto.2008.06.003':'https://pubmed.ncbi.nlm.nih.gov/18662886/',
#        '10.1016/j.cyto.2008.01.001':'https://pubmed.ncbi.nlm.nih.gov/18321765/',
#        '10.1016/j.cyto.2008.02.005':'https://pubmed.ncbi.nlm.nih.gov/18362077/',
#        '10.1016/j.cyto.2009.07.004':'https://pubmed.ncbi.nlm.nih.gov/19660963/',
#        '10.1016/j.cyto.2008.12.021':'https://pubmed.ncbi.nlm.nih.gov/19231232/',
#        '10.1016/j.cyto.2008.12.013':'https://pubmed.ncbi.nlm.nih.gov/19251437/',
#        '10.1016/j.cyto.2008.12.015':'https://pubmed.ncbi.nlm.nih.gov/19223199/',
#        '10.1016/j.cyto.2011.06.006':'https://pubmed.ncbi.nlm.nih.gov/21733716/',
#         '10.1016/j.cyto.2011.08.017':'https://pubmed.ncbi.nlm.nih.gov/21890375/',
#         '10.1016/j.cyto.2011.02.016':'https://pubmed.ncbi.nlm.nih.gov/21419645/',
#        '10.1016/j.cyto.2011.06.005':'https://pubmed.ncbi.nlm.nih.gov/21742513/',
#         '10.1016/j.cyto.2012.08.025':'https://pubmed.ncbi.nlm.nih.gov/23017228/',
#        '10.1016/j.cyto.2013.04.009':'https://pubmed.ncbi.nlm.nih.gov/23664770/',
#         '10.1016/j.cyto.2013.04.005':'https://pubmed.ncbi.nlm.nih.gov/23612013/',
#         '10.1016/j.cyto.2014.07.249':'https://pubmed.ncbi.nlm.nih.gov/25127907/',
#         '10.1038/34214':'https://pubmed.ncbi.nlm.nih.gov/9422513/',
#     '10.1038/44188':'https://pubmed.ncbi.nlm.nih.gov/10524633/',
#     '10.1038/nature07034':'https://pubmed.ncbi.nlm.nih.gov/18552838/',
#        '10.1038/nature07091':'https://pubmed.ncbi.nlm.nih.gov/18594509/',
#        '10.1038/nature08027':'https://pubmed.ncbi.nlm.nih.gov/19483678/',
#        '10.1038/nature10539':'https://pubmed.ncbi.nlm.nih.gov/22012259/',
#        '10.1038/nature12878':'https://pubmed.ncbi.nlm.nih.gov/24336215/',
#        '10.1038/onc.2013.184':'https://pubmed.ncbi.nlm.nih.gov/23728342/',
#        '10.1038/onc.2013.237':'https://pubmed.ncbi.nlm.nih.gov/23770856/',
#        '10.1038/onc.2014.404':'https://pubmed.ncbi.nlm.nih.gov/25531324/',
#        '10.1038/onc.2014.22':'https://pubmed.ncbi.nlm.nih.gov/24632608/',
#        '10.3892/ijo.2012.1714':'https://pubmed.ncbi.nlm.nih.gov/23175173/',
#        '10.3892/ijo.2012.1617':'https://pubmed.ncbi.nlm.nih.gov/27826623/',
#        '10.3892/ijo.2012.1470':'https://pubmed.ncbi.nlm.nih.gov/22581300/',
#        '10.3892/ijo.2012.1343':'https://pubmed.ncbi.nlm.nih.gov/22293778/',
#        '10.3892/ijo.2013.1789':'https://pubmed.ncbi.nlm.nih.gov/23354006/',
#        '10.3892/ijo.2012.1741':'https://pubmed.ncbi.nlm.nih.gov/23254774/',
#        '10.3892/ijo.2013.1761':'https://pubmed.ncbi.nlm.nih.gov/23292068/',
#         '10.3892/ijo.2013.1809':'https://pubmed.ncbi.nlm.nih.gov/23403907/',
#        '10.3892/ijo.2013.1903':'https://pubmed.ncbi.nlm.nih.gov/23588792/',
#        '10.1016/j.ccr.2013.04.019':'https://pubmed.ncbi.nlm.nih.gov/23727022/',
#        '10.1016/j.ccr.2012.10.003':'https://pubmed.ncbi.nlm.nih.gov/23153534/',
#        '10.1016/j.ccr.2013.12.007':'https://pubmed.ncbi.nlm.nih.gov/24434208/',
#        '10.1016/j.ccr.2013.02.018':'https://pubmed.ncbi.nlm.nih.gov/23597563/',
#        '10.1016/j.ccell.2014.09.008':'https://pubmed.ncbi.nlm.nih.gov/25446900/',
#        '10.1073/pnas.1101273108':'https://pubmed.ncbi.nlm.nih.gov/21383157/',
#        '10.1073/pnas.1108537109':'https://pubmed.ncbi.nlm.nih.gov/22451918/',
#        '10.1073/pnas.1202214109':'https://pubmed.ncbi.nlm.nih.gov/22492977/',
#        '10.1073/pnas.1310331110':'https://pubmed.ncbi.nlm.nih.gov/23798383/',
#         '10.1073/pnas.1211179110':'https://pubmed.ncbi.nlm.nih.gov/23302695/',
#        '10.1073/pnas.1319190110':'https://pubmed.ncbi.nlm.nih.gov/24367099/'
#       }
