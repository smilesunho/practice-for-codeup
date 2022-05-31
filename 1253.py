#!/usr/bin/env python
# coding: utf-8

# In[55]:
'''
어떤 두 수 a, b가 있을 때 두 수 사이의 모든 정수를 오름차순으로 출력하시오.
예를 들어, a=5 , b=10일 경우 5 6 7 8 9 10입니다
'''

a,b=input().split(" ") 
a=int(a)
b=int(b)
c=a-b
if c>0:
    a1=b
    b1=a
elif c<0:
    a1=a
    b1=b
    c=c*-1
else :
    if a>b:
        a1=b
        b1=a
        c=b
    elif a<b:
        a1=a
        b1=b
        c=a
    else:
        print(a)
for i in range(0,c+1):
    print(a1+i,end=" ")
    

