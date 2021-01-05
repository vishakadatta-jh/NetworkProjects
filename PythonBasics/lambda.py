#!/usr/bin/env python
# coding: utf-8

# In[1]:


"no need of return function"


# In[2]:


a = lambda x,y:x*y


# In[3]:


a(2,2)


# In[4]:


int a


# In[21]:


def func(list0):
    list1 = []
    for i in range(1,5):
        result = i * 2
        list1.append(result)
    return list1 + list0


# In[10]:


list0 = [i for i in range(10) if i%2 != 0]


# In[11]:


list0


# In[22]:


func(list0)


# In[23]:


"instead of all these use LAMBDA!!!!!"


# In[33]:


lambda_a = lambda list0: [i * 2 for i in range(1,5)] + list0


# In[34]:


lambda_a(list0)


# In[ ]:




