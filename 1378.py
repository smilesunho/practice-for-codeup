#!/usr/bin/env python
# coding: utf-8

# In[10]:


'''
동렬이는 수학 문제를 풀다 다음과 같은 수열을 보았다.

Sn=(1)+(1+2)+(1+2+3)+(1+2+3+4)+...+(1+...+n)
임의의 정수 n이 주어질 때 이 수열의 합 Sn을 구하는 프로그램을 작성하시오.
'''
a=input().strip()
a=int(a)
b=[]
for i in range(1,a+1):
    for j in range(1,i+1):
        b.append(j)
print(sum(b))


# In[ ]:




