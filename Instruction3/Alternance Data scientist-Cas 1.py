#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[1]:


import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import time
import csv
import pandas as pd


# In[2]:


driver=webdriver.Chrome("C:/seleniumdriver/chromedriver")
url = "https://www.welcometothejungle.com/fr/jobs?query=&groupBy=job&sortBy=mostRelevant&aroundQuery=&refinementList%5Bcontract_type_names.fr%5D%5B%5D=CDD%20%2F%20Temporaire&refinementList%5Bcontract_type_names.fr%5D%5B%5D=CDI&refinementList%5Bcontract_type_names.fr%5D%5B%5D=Stage&refinementList%5Bcontract_type_names.fr%5D%5B%5D=Temps%20partiel&refinementList%5Bcontract_type_names.fr%5D%5B%5D=Alternance&refinementList%5Bsectors_name.fr.Tech%5D%5B%5D=SaaS%20%2F%20Cloud%20Services&refinementList%5Bsectors_name.fr.Tech%5D%5B%5D=Logiciels&refinementList%5Bsectors_name.fr.Tech%5D%5B%5D=Big%20Data&refinementList%5Bsectors_name.fr.Tech%5D%5B%5D=Cybers%C3%A9curit%C3%A9&refinementList%5Bsectors_name.fr.Tech%5D%5B%5D=Application%20mobile&refinementList%5Bsectors_name.fr.Tech=&page=1"
driver.get(url) 


# Scrapper la data contenue dans la premiere page

# In[3]:


# [@id="title"]

Company=driver.find_elements_by_css_selector('.sc-7dlxn3-6')
job=driver.find_elements_by_css_selector('.sc-7dlxn3-5 .ais-Highlight-nonHighlighted')

# Pour parcourir les attribues des elements :
time=driver.find_elements_by_css_selector('.sc-1lvyirq-3  time')
times=[]
for i in range(len(time)):
    times.append(time[i].get_attribute("datetime"))
#     ---------------------------------------
Link=driver.find_elements_by_css_selector('.sc-7dlxn3-4  a')
jobL=[]
for i in range(len(Link)):
    jobL.append(Link[i].get_attribute("href"))
    
# print(timestamp)


# In[4]:


Companyname=[]
for i in range(len(Company)):
    Companyname.append(Company[i].text)
# Companyname
# --------------------------------------
jobTitle=[]
for i in range(len(job)):
    jobTitle.append(job[i].text)
# jobTitle
# ----------------------------------------
jobLink=[]
for i in range(len(jobL)):
    jobLink.append(jobL[i])
# jobLink
# ------------------------------------
timestamp=[]
for i in range(len(times)):
    timestamp.append(times[i])
print(len(jobLink))

# details=[]
# for i in range(len(CompanyName)):
#     informations={}
#     informations['CompanyName']=CompanyName[i].text
#     informations['jobTitle']=jobTitle[i].text
#     informations['jobLink']=jobLink[i] 
#     informations['timestamp']=timestamp[i]
#     details.append(informations)
# details


# In[5]:


jobLocation=[]
jobDescription=[]
jobType=[]
driver=webdriver.Chrome("C:/seleniumdriver/chromedriver")
for i in range(len(jobL)):
    url = jobL[i]
    driver.get(url) 
    dlocation=driver.find_elements_by_css_selector('ul.sc-1lvyirq-4 > li:nth-child(2) .k0cd2-4.gxOAwV')
    if(dlocation):
        jobLocation.append(driver.find_elements_by_css_selector('ul.sc-1lvyirq-4 > li:nth-child(2) .k0cd2-4.gxOAwV')[0].text)
    else:
        jobLocation.append('NaN')
    jobDescription.append(driver.find_elements_by_css_selector('#description-section .sc-1yj8948-1')[0].text)
    # jobExperience=driver.find_elements_by_css_selector('.sc-1lvyirq-3 span')
    # jobRef=driver.find_elements_by_css_selector('')
    jobType.append(driver.find_elements_by_css_selector('ul.sc-1lvyirq-4 > li:nth-child(1) .sc-1lvyirq-3.kqrath')[0].text)
    


# In[6]:


for i in range(len(jobType)):
    print(jobType[i])


# In[7]:


jobLink


# In[8]:


t=[]
for i in range(len(jobLocation)):
    print(jobLocation[i])


# In[9]:


# split pour repartir je joblink en 2 parties sous forme de tableau
jobRef=[]
for i in range(len(jobLink)):
    jobRef.append(jobLink[i].split("o=")[1])
jobRef


# In[238]:


timestamp


# In[10]:


# Obtenir la colonne postDate en se basant sur timestamp en prenant selement la date
# et formater timestamp en remplaçant T par espace 
from datetime import datetime
postDate=[]
Timestamp=[]
for i in range(len(timestamp)):
    Timestamp.append(timestamp[i].split(".")[0].replace("T"," "))
    postDate.append(timestamp[i].split("T")[0])
print(postDate)


# In[247]:


print(Timestamp)


# In[ ]:





# In[11]:


df=pd.DataFrame(list(zip(Companyname, jobDescription, jobLink, jobLocation, jobRef, jobTitle, jobType, postDate, Timestamp)),columns=['Companyname', 'jobDescription', 'jobLink', 'jobLocation', 'jobRef', 'jobTitle', 'jobType', 'postDate', 'Timestamp'])


# In[ ]:


df.to_excel('test.xlsx')


# In[12]:


default=[]
for i in range(len(Companyname)):
    default.append('ACCOUNT EXCECUTIVE')


# In[13]:


DF=pd.DataFrame(list(zip(Companyname,default, jobDescription, jobLink, jobLocation, jobRef, jobTitle, jobType, postDate, Timestamp)),columns=['Companyname', 'jobCorrespondance', 'jobDescription', 'jobLink', 'jobLocation', 'jobRef', 'jobTitle', 'jobType', 'postDate', 'timestamp'])
DF


# In[16]:


# DF.to_excel('C:/Users/Hajar/Downloads/Alternance Data scientist - Cas 1.xlsx', sheet_name='wttj jobs offers')


# In[17]:


import os
import openpyxl

def append_data_to_excel(file_name, sheet_name, data):
    # check if file exists
    if os.path.isfile(file_name):
        # load existing workbook
        book = openpyxl.load_workbook(file_name)
        writer = pd.ExcelWriter(file_name, engine='openpyxl')
        writer.book = book
        writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
        # write dataframe to existing sheet
        data.to_excel(writer, sheet_name, index=False)
        writer.save()
        writer.close()
    else:
        # create new workbook
        writer = pd.ExcelWriter(file_name, engine='openpyxl')
        # write dataframe to new sheet
        data.to_excel(writer, sheet_name)
        writer.save()


# In[ ]:


append_data_to_excel('C:/Users/Hajar/Downloads/Alternance Data scientist - Cas 1.xlsx', 'wttj jobs offers', DF)


# In[333]:





# In[ ]:





# In[ ]:





# In[ ]:




