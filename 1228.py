#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
희윤이의 키와 몸무게가 공백을 기준으로 입력된다.(실수)
희윤이의 비만도에 따른 등급을 출력한다.(설명 참조)
'''
a,b=map(float,input().split(" "))
c=(a-100)*0.9
j=(b-c)*100/c
if j<=10:
    print("정상")
elif 10<j and j<=20:
    print("과체중")
else:
    print("비만")

        


# In[ ]:




