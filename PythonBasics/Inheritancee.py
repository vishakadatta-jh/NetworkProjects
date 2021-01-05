#!/usr/bin/env python
# coding: utf-8

# In[8]:


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


# In[19]:


class MyNewRouter(MyRouter):
    "new class inherited by MyRouter"
    def __init__(self,routername,model,serialno,ios,portno):
        MyRouter.__init__(self,routername,model,serialno,ios)
        self.portno = portno
    def new_router(self,string):
        print("newrouter",self.routername)


# In[14]:





# In[20]:


newrr = MyNewRouter("cisco","12.23","123345","34.90","8089")


# In[17]:


newrr.portno


# In[21]:


newrr.new_router("whatver")


# In[ ]:




