#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
1. 5개의 자연수가 공백으로 구분되어 입력된다.
2. 각 정수는 0보다 크고 100보다 작다.
3. 입력되는 수는 모두 다른 수이다.

1. 중앙값을 출력한다.
'''
b=list(map(int,input().split(" ")))
b=sorted(b)
print(b[2])


# In[ ]:




