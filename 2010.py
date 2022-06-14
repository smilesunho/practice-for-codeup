#!/usr/bin/env python
# coding: utf-8

# In[14]:


'''
양의 정수 B와 N이 입력되면, A^N이 B와 가장 가까운 수가 되는 A를 출력하시오.
A^N은 B보다 크거나 작거나 같다.
'''
b,n=map(int,input().split(" "))
a=1
while a**n<b:
    a=a+1
if (a+1)**n==b:
    print(a)
elif (((a)**n)-b)<(b-((a-1)**n)):
        print(a)
else:
    print(a-1)

    
  

