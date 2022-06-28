#!/usr/bin/env python
# coding: utf-8

# In[20]:


'''
세 개의 숫자가 주어질 때 작은 순서로 나열 했을 때, 두번째 수를 출력해보자.
'''
a=list(map(int,input().strip().split(" ")))
a=sorted(a)
print(a[1])


# In[ ]:




