#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
세 정수를 입력받아 입력받은 순서의 역순으로 출력하시오.
예)
3 5 4   ----> 4 5 3
'''
a=list(map(int,input().split(" ")))
for i in range(2,-1,-1):
    print(a[i], end=' ')


    
  

