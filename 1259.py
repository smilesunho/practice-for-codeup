#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
1부터 n까지의 수 중 짝수의 합을 구하시오..
'''
a=int(input())
b=[]
for i in range(1,a+1):
    if i%2==0:
        b.append(i)
print(sum(b))
    


# In[ ]:




