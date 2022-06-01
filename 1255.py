#!/usr/bin/env python
# coding: utf-8

# In[75]:
'''
소수 둘째 자리의 두 실수 a와 b가 입력으로 주어진다.
a와 b사이의 수를 0.01간격으로 오름차순으로 출력하시오.
예)
5.67 5.73  ==> 5.67 5.68 5.69 5.70 5.71 5.72 5.73
'''

a,b=input().split(" ") 
a=float(a)
b=float(b)
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
        
while a1<b1:
    print('{:.2f}'.format(a1),end=" ")
    a1=0.01+a1


# In[ ]:




