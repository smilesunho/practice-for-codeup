#!/usr/bin/env python
# coding: utf-8

# In[34]:


'''
첫째줄에 N이 입력된다. (1<=N<=10,000)
다음 줄부터 N개의 데이터가 한 줄에 한 개씩 입력된다.
'''
a=int(input())
k=[]
i=0
while i<a:
    b=int(input())
    k.append(b)
    i=i+1
k=sorted(k)
for i in k:
    print(i)


# In[ ]:




