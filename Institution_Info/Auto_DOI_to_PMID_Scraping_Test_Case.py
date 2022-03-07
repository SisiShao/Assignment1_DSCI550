#!/usr/bin/env python
# coding: utf-8

# # The purpose of this test case is to convince you the method described in *Auto_DOI_To_PMID_API.ipynb* through randomly picking one DOI, in this case is *'10.1002/ijc.27627'*.

# In[1]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


e = '10.1002/ijc.27627'
PMID = {}


# In[3]:



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.pmid2cite.com/doi-to-pmid-converter")
try:
    button = driver.find_element_by_xpath('//input[@placeholder="Please enter DOI"]').send_keys(e)
    button2 = driver.find_element_by_xpath('//button').click()
    result = driver.find_elements_by_xpath('//a[@target="_blank"]')
    for r in result:
        if r.text != '':
            PMID[e] = r.text.strip()
except:
    PMID[e] = 'NA'


# In[4]:


PMID

