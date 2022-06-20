#!/usr/bin/env python
# coding: utf-8

# In[57]:


'''
정수 두개가 입력된다.(최대 100자리) - 같은 숫자는 입력되지 않는다.
작은수 큰수 순서로 출력한다.
'''
a,b=input().strip().split(" ")
a=str(a)
b=str(b)
if len(a)>len(b):
    print(b,a)
elif len(a)<len(b):
    print(a,b)
else:
    i=0
    while i<1:
        for k in range(0,len(a)):
            if int(a[k])==int(b[k]):
                pass
            else :
                if int(a[k])>int(b[k]):
                    print(b,a)
                    i=i+1
                    break
                else:
                    print(a,b)
                    i=i+1
                    break

