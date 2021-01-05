#!/usr/bin/env python
# coding: utf-8

# In[5]:


list1 = [i for i in range(1,10,2)]


# In[7]:


list1


# In[15]:


iterator = iter(list1)


# In[16]:


next(iterator)


# In[17]:


generator = (i for i in range(5))


# In[19]:


type(generator)


# In[21]:


next(generator)


# In[23]:


from itertools import *


# In[25]:


list1= [1,2,3,'a','b','c']


# In[26]:


list2= [10,20,30,'az','sb','qc']


# In[28]:


chain(list1,list2)


# In[29]:


list(chain(list1,list2))


# In[32]:


for i  in count(10,2.5):
    if i<90:
        print (i)
    else:
        break


# In[ ]:


a = range(10,19)


# In[ ]:


for i in a:
        print (i)


# In[37]:


list(filterfalse(lambda x:x<5,[1,2,3,4,5,6,7,8,9,0]))


# In[38]:


aa = list(range(10))[2:9:2]


# In[39]:


print (aa)


# In[41]:


ao=islice(range(10),2,9,2)


# In[42]:


ao


# In[ ]:





# In[ ]:





# In[ ]:




