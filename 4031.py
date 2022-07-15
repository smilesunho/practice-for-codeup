#!/usr/bin/env python
# coding: utf-8

# In[4]:


'''
1. 첫 번째 줄에 7개의 자연수가 공백으로 구분되어 주어진다.
2. 입력되는 수는 100보다 작은 수이다

1. 홀수로서 가장 큰 수와 짝수로서 가장 큰 수를 각각 찾아 그 합을 출력한다
'''
import numpy as np 
b=list(map(int,input().split(" ")))
a=[]
c=[]
for i in b:
    if i%2==0:
        a.append(i)
    else:
        c.append(i)

if len(a)==0:
    a.append(0)

if len(c)==0:
    c.append(0)

print(np.max(a)+np.max(c))





# In[ ]:




