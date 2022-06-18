#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
n은 자연수, 그 다음 줄에 n개의 자연수들이 입력으로 들어온다.
n개의 자연수들 중 짝수의 개수를 출력한다.
'''
a=input()
a=int(a)
b=list(map(int,input().strip().split(" ")))
w=0
for i in b:
    if i%2==0:
        w=w+1
print(w)

