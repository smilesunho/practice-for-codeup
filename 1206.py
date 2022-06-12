#!/usr/bin/env python
# coding: utf-8

# In[13]:


'''
두 자연수 a, b가 주어진다.
b가 a의 배수이면 "a*x=b"를 출력하고,
a가 b의 배수이면 "b*x=a"를 출력하고,
배수관계가 아니면 "none"을 출력하시오.
'''
a,b=map(int,input().split(" "))
if a%b==0:
    x=a//b
    print("{0}*{1}={2}".format(b,x,a))
elif b%a==0:
    x=b//a
    print("{0}*{1}={2}".format(a,x,b))
else:
    print("none")

        


# In[ ]:




