#!/usr/bin/env python
# coding: utf-8

# In[101]:
'''
5개의 정수들의 최댓값과 최솟값을 구하는 프로그램을 작성하라.
'''

import numpy as np
a=[]
b=[]
for i in range(0,5):
    a.append(input())
a=sorted(a)
a=np.array(a,dtype=np.int64)
x=max(a)
n=min(a)
print(x)
print(n)


# In[ ]:




