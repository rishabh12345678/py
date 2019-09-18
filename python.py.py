#!/usr/bin/env python
# coding: utf-8

# In[3]:


l1 = ['hello','hi',24,67]
l1


# In[6]:


l2 = ['rishabh','wow',34]
l1.extend(l2)
l1


# In[8]:


l1.extend([45,75,65])
l1


# In[10]:


l1.insert(1,'hdjhd')
l1


# In[11]:


l2 = ['come','on','what']
l1.insert(3,l2)
l1


# In[12]:


del l1[3]
l1


# In[13]:


l1.remove('wow')
l1


# In[15]:


s = len(l1)
s


# In[16]:


s2 = l1.len()
s2


# In[17]:


f = l1[-6:-2]
f


# In[21]:


g = l1[:5]
g


# In[23]:


h = l1[5][0]
h


# In[25]:


for x in l1:
    print (x)


# In[26]:


dc = {'name':'rishabh','age':22,'college':'GU'}
dc


# In[27]:


for x in dc:
    print (x)
    


# In[28]:


for x in dc.values():
    print(x)
    


# In[32]:


for x,y in dc.items():
    print(x,y)


# In[31]:


dc['age']= 21
dc


# In[33]:


a = len(dc)
a


# In[34]:


dc['city']= 'lucknow'
dc


# In[35]:


del dc['age']
dc


# In[36]:


cd = dc.copy()
cd


# In[39]:


x = dict({'human':21,'jssj':45,'sjksj':55})
x


# In[43]:


an1 = {'name':'rishabh','age':22,'college':'gu'}
an2 = {'name':'deepak','age':22,'college':'gu'}
an3 = {'name':'khaja','age':20,'college':'dkjcn'}
x ={y:an1,y2:an2,y3:an3}
x


# In[ ]:




