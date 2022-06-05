#!/usr/bin/env python
# coding: utf-8

# In[4]:
'''
정수 a, b가 공백으로 분리되어 입력된다.(-10,000 <= a, b <=10,000)
연산 결과의 중앙값을 출력한다.
'''

a,b=input().split(" ")
a=int(a)
b=int(b)
c=(a+b)
d=(a-b)
e=(a*b)
k=[c,d,e]
k=sorted(k)
print(k[1])

