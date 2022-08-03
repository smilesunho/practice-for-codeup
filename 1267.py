#!/usr/bin/env python
# coding: utf-8

# In[20]:


'''
첫째 줄에 정수 n이 입력된다.(1<=n<=1,000)

둘째 줄에 n개의 자연수들이 공백으로 분리되어 입력된다. 각 정수는 1~1,000 사이이다.

n개의 자연수들 중 5의 배수의 합을 출력한다.

'''
a=input()
b=list(map(int,input().strip().split(" ")))
k=[0]
for i in b:
   if i%5==0:
       k.append(i)
print(sum(k))


# In[ ]:




