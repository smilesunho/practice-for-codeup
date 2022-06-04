#!/usr/bin/env python
# coding: utf-8

# In[19]:
'''
첫 째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100보다 작다 
첫째 줄에 최대값을 출력하고, 둘째 줄에 최대값이 몇 번째 수인지를 출력한다. 
'''

a=0
c=1
d={}
while a<9:
    b=input()
    b=int(b)
    d[c]=b
    c=c+1
    a=a+1
max_key=max(d,key=d.get)
print(d[max_key])
print(max_key)

