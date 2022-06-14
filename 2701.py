#!/usr/bin/env python
# coding: utf-8

# In[6]:


'''
첫 번째 줄에 당신의 위치 X가 주어진다.(0<=X<=500)
두 번째 줄에 비상구의 위치 5개가 오름차순으로 주어진다.

당신의 위치와 가장 가까운 비상구까지의 거리를 출력하시오.
'''
a=int(input())
b=list(map(int,input().strip().split(" ")))
c=[]
for i in range(0,len(b)):
    c.append(abs(a-b[i]))
c=sorted(c)
print(c[0])


# In[ ]:




