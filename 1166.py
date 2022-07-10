#!/usr/bin/env python
# coding: utf-8

# In[7]:


'''
2월이 29일까지 있는 해를 윤년이라고 한다.
한 자연수를 입력받아서 윤년인지 아닌지를 판단하는 프로그램을 작성하시오.
단, 윤년은 다음과 같은 성질을 지닌다고 한다.

(1) 400의 배수이면 무조건 윤년이다.
(2) (1)이 아닌 수 중에 4의 배수이며, 100의 배수가 아니면 윤년이다.
'''
a=input()
a=int(a)
if a%400==0:
    print("Leap")
elif a%4==0 and a%100!=0:
    print("Leap")
else:
    print("Normal")


# In[ ]:




