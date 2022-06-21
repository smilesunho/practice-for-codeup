#!/usr/bin/env python
# coding: utf-8

# In[45]:


'''
첫째 줄에는 입력되는 수열의 길이를 나타내는 정수 N이 주어진다.
둘째 줄에는 공백으로 구분된 N개의 정수 Si가 차례로 주어진다.
[입력값의 정의역]
3≤N≤10,000
0<=Si<=32767

첫째 줄에는 수열의 최댓값의 위치와 ":"과 최댓값을 공백으로 구분하여 출력한다.
둘째 줄에는 수열의 최솟값의 위치와 ":"과 최솟값을 공백으로 구분하여 출력한다.
(단, 최대값이나 최소값이 여러 개 있을 경우에는 제일 먼저나오는 위치 및 값을 출력한다.)
'''
import numpy as np
a=input()
a=int(a)
b=list(map(int,input().strip().split(" ")))
d={}
i=1
for k in b:
    d[i]=k
    i=i+1

def get_key(val):
    for key, value in d.items():
         if val == value:
                return key


l1=list(d.values())
a1=(np.max(l1))
a2=(np.min(l1))
print(get_key(a1),":",a1)
print(get_key(a2),":",a2)


# In[ ]:




