#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
태어난 해, 월, 일을 입력받아 사주팔자를 보는 프로그램을 작성하시오.

사주를 보는 방법)

세 수(년,월,일)가 주어지면,  (년 + 월 + 일)에 100의 자리 숫자가 짝수이면 "대박"을 출력, 그렇지 않으면 "그럭저럭"을 출력하세요..
'''

a,b,c=input().strip().split(' ')
a=int(a)
b=int(b)
c=int(c)
d=a+b+c
d=str(d)
e=int(d[-3])

if e%2==0:
    print("대박")
else:
    print("그럭저럭")


# In[ ]:




