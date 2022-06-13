#!/usr/bin/env python
# coding: utf-8

# In[7]:


'''
두 자연수 a, b 사이의 구간에 대해서
홀수는 더하고 짝수는 뺀다음의 합을 출력하시오.
'''
a,b=map(int,input().strip().split(" "))
c=[]
for i in range(a,b+1):
    if i%2==0:
        c.append(i*-1)
    else:
        c.append(i)
print(sum(c))
    


# In[ ]:




