#!/usr/bin/env python
# coding: utf-8

# In[12]:


class MyRouter(object):
    "this is a class of router"
    def __init__(self,routername,model,serialno,ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios
        
    def print_router(self,manf_date):
        print("routername",self.routername)
        print("model",self.model + manf_date)
        print("serialno",self.serialno )
        print("ios & model",self.ios + self.model)


# In[17]:


router1 = MyRouter('CISCO','223K9','123343','IP8.9')


# In[3]:


router1


# In[4]:


router1.ios


# In[13]:


router1.print_router('12/2/2099')


# In[14]:


haha.print_router("909090")


# In[20]:


getattr(router2,"ios")


# In[19]:


router2 = MyRouter('ok','ok1','oo','')


# In[21]:


setattr(router2,"ios","99.ip")


# In[26]:


hasattr(router2,"ios")


# In[25]:


delattr(router2,"ios")


# In[27]:


router2.print_router("9090")


# In[28]:


isinstance(router2,MyRouter)


# In[ ]:




