#!/usr/bin/env python
# coding: utf-8

# In[10]:


'''
첫째 줄에 N과 K가 빈칸을 사이에 두고 주어진다. 
N은 1 이상 10,000 이하이다. K는 1 이상 N 이하이다.
첫째 줄에 N의 약수들 중 K번째로 작은 수를 출력한다. 
만일 N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 
0을 출력하시오.

'''
n,k=input().strip().split(" ")
n=int(n)
k=int(k)
b=[]
for i in range(1,n):
    if n%i==0:
        b.append(i)
if len(b)==0:
    print("0")
elif len(b)<k:
    print("0")
else :
    print(b[k-1])
    


# In[ ]:




