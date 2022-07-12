#!/usr/bin/env python
# coding: utf-8

# In[5]:


'''
두 정수를 입력받아 아래와 같이 출력하시오.

예)  3 2

3+2=5
3-2=1
3*2=6
3/2=1

'''
a,b=input().strip().split(" ")
a=int(a)
b=int(b)

print('{0}+{1}={2}'.format(a,b,a+b))
print('{0}-{1}={2}'.format(a,b,a-b))
print('{0}*{1}={2}'.format(a,b,a*b))
print('{0}/{1}={2}'.format(a,b,int(a/b)))


# In[ ]:




