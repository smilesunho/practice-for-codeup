#!/usr/bin/env python
# coding: utf-8

# In[15]:
'''
팩토리얼(!)은 다음과 같이 정의된다.

n! = n * (n-1) * (n-2) * ... * 2 * 1

즉, 5! = 5 * 4 * 3 * 2 * 1 = 120 이다.

n이 입력되면 n!의 값을 출력하시오.

'''

a=input()
a=int(a)
k=0
for i in range(a,0,-1):
    if i==a:
        k=a
    else :
        k=k*i
print(k)


# In[ ]:




