#!/usr/bin/env python
# coding: utf-8

# In[87]:


'''
첫 번째 줄에 코드표의 문자 10개가 주어진다. 
(순서대로 0~9이다. 알파벳 소문자만 입력됨. 중복x)
두번째 줄에 암호화된 전화번호 3블럭이 띄워쓰기로 구분되어 입력된다.

0	1	2	3	4	5	6	7	8	9
l	o	h	c	g	p	d	a	b	k
'''
a=input().strip()
b,d,f=input().strip().split(" ")
c={}
for i in range(0,10):
    c[a[i]]=str(i)
h=[]
j=[]
e=[]
for k in b:
    h.append(c[k])
for k in d:
    j.append(c[k])
for k in f:
    e.append(c[k])
print(''.join(h)+' '+''.join(j)+' '+''.join(e))

    

