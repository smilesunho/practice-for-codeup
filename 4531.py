#!/usr/bin/env python
# coding: utf-8

# In[6]:


'''
첫 째 줄부터 다섯 번째 줄까지 한 줄에 하나씩 자연수가 주어진다. 주어지는 자연수는 100보다 작은 10의 배수이다. 

첫째 줄에는 평균을 출력한다. 둘째 줄에는 중앙값을 출력한다. 평균과 중앙값은 모두 자연수이다.
'''
import numpy as np 
i=0
b=[]
while i<5:
    a=input()
    a=int(a)
    b.append(a)
    i=i+1

print(int(np.mean(b)))
print(int(np.median(b)))





# In[ ]:




