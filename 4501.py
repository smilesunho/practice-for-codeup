#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
7명의 난장이의 키가 입력으로 주어질때 이 중 키가 가장 큰 난장이와 
두 번째로 큰 난장이의 키를 출력하는 프로그램을 작성하시오.
'''
i=1
b=[]
while i<=7:
    a=input()
    a=int(a)
    b.append(a)
    i=i+1
b=sorted(b)
print(b[6])
print(b[5])


# In[ ]:




