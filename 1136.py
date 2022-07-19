#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
두 정수 a, b가 공백을 두고 입력된다.(a,b는 int형 범위)

a와 b가 같을 경우 1, 그렇지 않은 경우 0을 출력한다.

'''

a,b=input().strip().split(" ")
a=int(a)
b=int(b)
if a==b:
    print("1")
else:
    print("0")


# In[ ]:




