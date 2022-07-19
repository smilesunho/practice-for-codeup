#!/usr/bin/env python
# coding: utf-8

# In[8]:


'''
두 정수가 입력된다.

두 정수의 값이 모두 참(1) 이면 참(1), 하나라도 거짓(0)이면 거짓(0)을 출력한다..

'''

a,b=input().strip().split(" ")
a=int(a)
b=int(b)

if a==1 and b==1:
    print('1')
else:
    print('0')


# In[ ]:




