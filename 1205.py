#!/usr/bin/env python
# coding: utf-8

# In[53]:


'''
두 실수 a, b가 입력되면 그 두수를 더하거나 빼거나 곱하거나 나누거나 제곱을 해서 
가장 큰 수를 출력하시오.
'''
a,b=map(float,input().split(" "))
c=[]
c.append(a-b)
c.append(a+b)
c.append(a*b)
c.append(a/b)
c.append(a**b)
c.append(b-a)
c.append(b+a)
c.append(b*a)
c.append(b/a)
c.append(b**a)
print("{:0.6f}".format(max(c)))


# In[ ]:




