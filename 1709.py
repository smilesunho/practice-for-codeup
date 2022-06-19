#!/usr/bin/env python
# coding: utf-8

# In[47]:


'''
첫줄에는 데이터의 개수를 입력받는다.(100이하의 정수)
다음 줄에는 데이터가 입력된다.(100이하의 정수)
정렬된 데이터가 출력된다.
'''
a=input().strip().split(" ")
b=map(int,input().strip().split(" "))
b=list(b)
b=sorted(b)
b.reverse()
for i in b:
    print(i,end=' ')
    

