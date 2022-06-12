#!/usr/bin/env python
# coding: utf-8

# In[12]:


'''
입력의 개수 n이 입력되고 n개의  데이터가 입력된다.
이 n개의 데이터 중 최댓값을 출력한다.
'''
a=int(input())
b=input().strip().split(" ")
b=list(map(int,b))
print(max(b))


# In[ ]:




