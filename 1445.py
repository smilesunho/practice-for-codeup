#!/usr/bin/env python
# coding: utf-8

# In[36]:


'''
첫 줄에 두 배열의 크기 n, m이 입력된다.(두 배열의 크기는 각각 1000보다 작다)
두번째 줄에 첫 번째 배열의 원소들이 오름차순으로 정수로 입력된다.
세번째 줄에 두 번째 배열의 원소들이 오름차순으로 정수로 입력된다
'''
a=input().strip().split(" ")
a=list(map(int,a))
b=input().strip().split(" ")
b=list(map(int,b))
c=input().strip().split(" ")
c=list(map(int,c))
for i in sorted(b+c):
    print(i,end=" ")


# In[ ]:




