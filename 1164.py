#!/usr/bin/env python
# coding: utf-8

# In[4]:


'''
터널의 높이가 차례대로 3개 주어진다. (정수)

170보다 같거나 작으면 "CRASH"를 출력, 그 보다 크면 "PASS"를 출력하시오.
'''

a,b,c=input().split(" ")
a=int(a)
b=int(b)
c=int(c)
if a>170 and b>170 and c>170:
    print("PASS")
else:
    print("CRASH")
    


# In[ ]:




