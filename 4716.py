#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
각 역에서 내린 사람 수와 탄 사람 수가 빈칸을 사이에 두고 첫째 줄부터 열번째 줄까지 역 순서대로 한 줄에 하나씩 주어진다. 
 
첫째 줄에 최대 사람 수를 출력한다.  
'''

import numpy as np 
i=0
b=[]
d=0
while i<10:
    a,c=input().split(" ")
    a=int(a)
    c=int(c)
    e=c-a
    d=d+e
    b.append(d)
    e=0
    i=i+1

print(int(np.max(b)))


# In[ ]:




