#!/usr/bin/env python
# coding: utf-8

# In[111]:


'''
분자와 분모를 순서대로 입력받아
정수부분을 제외한 소수점 이하 10자리 숫자를 출력하시오.
'''
a,b=input().strip().split(" ")
a=int(a)
b=int(b)
c=a/b
d=a//b
k=int((c-d)*10000000000)
if (len(str(k)))<10:
    k=str(k)
    while (len(k))<10:
        k=str(0)+k
    print(k)
else:
    print(int((c-d)*10000000000))


# In[ ]:




