#!/usr/bin/env python
# coding: utf-8

# In[42]:


'''
① 윷의 4가지 상태가 공백으로 구분되어 입력된다.

② 윷의 상태가 0이면 뒤집어 지지 않은 상태, 1이면 뒤집어진 상태를 의미한다.
'''

a=list(map(int,input().strip().split(' ')))

b=sum(a)
if b==0:
    print('모')
elif b==1:
    print('도')
elif b==2:
    print('개')
elif b==3:
    print('걸')
else:
    print('윷')


# In[ ]:




