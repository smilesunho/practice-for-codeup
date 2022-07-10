#!/usr/bin/env python
# coding: utf-8

# In[5]:


'''
초를 입력받아 분 / 초의 형태로 출력하시오.

예)
60  ====>   1 0    (1분 0초를 뜻함)
70    ====>    1  10       (1분 10초를 뜻함)
'''
a=input()
a=int(a)
if a<60:
    print("0",a)
elif a==60:
    print("1 0")
else:
    print(a//60,a%60)


# In[ ]:




