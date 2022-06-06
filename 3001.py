#!/usr/bin/env python
# coding: utf-8

# In[10]:


'''
첫째 줄에 데이터의 개수 n이 입력된다.(1 <= n <= 100,000)
둘째 줄에 n개의 양의 정수 데이터가 공백으로 분리되어 입력된다.
셋째 줄에 찾고자 하는 특정데이터 정수k 가 입력된다.

k를 찾았으면 데이터 k의 위치를 출력하고, 찾지 못했으면 -1을 출력한다.
'''
a=input()
b=input().split(" ")
c=input()
c=int(c)
if str (c) not in b:
    print("-1")
else:
    for i in range(0,len(b)):
        if c==int(b[i]):
            print(i+1)
        else:
            pass

