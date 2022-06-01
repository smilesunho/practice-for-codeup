#!/usr/bin/env python
# coding: utf-8

# In[80]:
'''
n이 입력되면 다음과 같은 삼각형을 출력하시오.
예)
n 이 5 이면
*
**
***
****
*****
'''
n=int(input())
for i in range(1,n+1):
    print(i*'*')

