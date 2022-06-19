#!/usr/bin/env python
# coding: utf-8

# In[41]:


'''
길이(글자수)가 100이하인 문자열을 입력받아 공백을 제거하고 출력하시오..
'''
a=input().strip().split(" ")
b=[]
j=0
for i in a:
    c=i
    if j==0:
        k=c
        j=j+1
    else:
        k=k+c
print(k)
    
    

