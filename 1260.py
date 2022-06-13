#!/usr/bin/env python
# coding: utf-8

# In[5]:


'''
어떤 수 a, b가 주어진다.
a와 b의 관계는 a <= b 이다.
a에서 b까지의 수 중 3의 배수만 더하여 출력하시오.
'''
a,b=map(int,input().strip().split(" "))
c=[]
for i in range(a,b+1):
    if i%3==0:
        c.append(i)
print(sum(c))
    


# In[ ]:




