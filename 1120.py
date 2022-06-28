#!/usr/bin/env python
# coding: utf-8

# In[12]:


'''
세 수의 평균을 소수 둘째자리까지 출력하시오.
'''
import numpy as np
a=list(map(int,input().strip().split(" ")))
print("{:.2f}".format((np.mean(a))))


# In[ ]:




