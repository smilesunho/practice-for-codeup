#!/usr/bin/env python
# coding: utf-8

# In[15]:


'''
두 정수가 입력된다.

두 정수 중 하나의 값이 참(1) 이면 참(1), 그렇지 않으면 거짓(0)을 출력한다.

'''

a,b=input().strip().split(" ")
a=int(a)
b=int(b)

if a==0 and b==0:
    print('0')
else:
    print('1')


# In[ ]:




