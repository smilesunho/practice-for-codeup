#!/usr/bin/env python
# coding: utf-8

# In[97]:


'''
시작수 a와 마지막 수 b가 입력된다.
a와 b까지 1의 개수를 센다.
'''
a,b=input().strip().split(" ")
a=int(a)
b=int(b)
h=[]
for i in range(a,b+1):
    h.append(str(i))
k=''.join(h)    
f=0
for i in range(0,len(k)):
    if int(k[i])==1:
        f=f+1
print(f)
        

