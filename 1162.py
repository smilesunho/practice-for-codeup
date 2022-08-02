#!/usr/bin/env python
# coding: utf-8

# In[40]:


'''
세 정수가 입력으로 주어진다. 순서대로 년도, 월, 일 이다.
년도 - 월 + 일의 마지막 숫자가 0이면 "대박"을 , 그렇지 않으면 "그럭저럭"을 출력하시오.
'''

a,b,c=input().strip().split(' ')
a=int(a)
b=int(b)
c=int(c)
d=a-b+c
d=str(d)
e=d[-1]

if e=='0':
    print("대박")
else:
    print("그럭저럭")


# In[ ]:




