#!/usr/bin/env python
# coding: utf-8

# In[25]:


'''
그룹 제한 인원 n명과 n명의 능력치가 공백으로 분리되어 한줄에 입력된다.
제일 첫번째 수가 n이다.(1<=n<=20)
내림차순으로 자료를 정리하되, 
가장 높은 능력치를 가진 캐릭터와 ⌊1+n/2⌋번째로 높은 능력치를 가진 캐릭터와 
순서를 바꾼다.
'''
import numpy as np
a=list(map(int,input().strip().split(" ")))
b=a.pop(0)
a=sorted(a)
a.reverse()
c=int((1+b/2))

if len(a)==1:
    print(a[0])
else:
    k=a[0]
    j=a[c-1]
    a[0]=j
    a[c-1]=k

    for i in a:
        print(i, end=' ')


# In[ ]:




