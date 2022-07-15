#!/usr/bin/env python
# coding: utf-8

# In[10]:


'''
비만을 판단하기 위해서 BMI 수치가 필요하다.

BMI 수치가 입력되면 비만을 판단하시오.

* BMI에 따른 비만 판정

BMI 수치	비만 판정
~10 이하	정상
~20 이하	과체중
20 초과	비만
 
'''
a=input()
a=int(a)
if a<11:
    print("정상")
elif a<21:
    print("과체중")
else:
    print("비만")





# In[ ]:




