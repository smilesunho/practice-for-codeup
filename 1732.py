#!/usr/bin/env python
# coding: utf-8

# In[6]:


'''정수 a, b 두 개를 입력받아서 출력할 때,
첫째 줄에 a÷b의 소수점 첫째 자리까지 계산한 결과(몫)와
둘째 줄에 소수점 이하를 버린 나눗셈 결과(몫)를 출력하고,
셋째 줄에 ab의 결과를 출력하시오
'''
import numpy as np

a,b=input().strip().split(" ")
a=int(a)
b=int(b)
print(np.round(a/b,1))
print(a//b)
print(a**b)


# In[ ]:




