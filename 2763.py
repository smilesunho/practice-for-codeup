#!/usr/bin/env python
# coding: utf-8

# In[21]:
'''
두 양의 정수 a, b가 입력된다.(2<= a, b <=100,000)
서로 소이면 coprime 을 출력하고, 아니면 no 를 출력한다.

'''
a,b=input().split(" ")
a=int(a)
b=int(b)
z=[]
w=[]
if a==b:
    print("no")
else:
    for i in range(1,a):
        if a%i==0:
            z.append(i)
    for i in range(1,b):
        if b%i==0:
            w.append(i)
    new_list=[]
    for v in z:
        if v in w:
            new_list.append(v)
    if len(new_list)==1:
        print("coprime")
    else:
        print("no")


# In[ ]:




