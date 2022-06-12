#!/usr/bin/env python
# coding: utf-8

# In[29]:


'''
가로와 세로의 정수 길이를 3세트 입력 받는다. (단, 길이는 1000 이하의 양의 정수값)
넓이가 가장 넓은 운동장의 넓이를 출력한다.
'''
i=0
k=[]
while i<3:
    a,b=map(int,input().strip().split(" "))
    k.append(a*b)
    i=i+1
print(max(k))


# In[ ]:




