#!/usr/bin/env python
# coding: utf-8

# In[27]:


'''
﻿자연수 N이 입력된다. (1≤N≤1,000,000)

1. 첫째 줄에 뒤집은 수를 출력한다.

2. 둘째 줄에 각 자릿수의 합을 출력한다.
'''

a=input()
a=str(a)
b=[]
c=[]
for i in range (len(a)-1,-1,-1):
    b.append(int(a[i]))

j=len(b)
for k in b:
    c.append(k*10**(j-1))
    j=j-1
print(sum(c))
print(sum(b))


# In[ ]:




