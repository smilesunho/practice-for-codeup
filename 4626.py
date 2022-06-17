#!/usr/bin/env python
# coding: utf-8

# In[14]:


'''
첫째 줄에 문제의 개수 N (1 ≤ N ≤ 100)이 주어진다.

둘째 줄에는 N개 문제의 채점 결과를 나타내는 0 혹은 1이 빈 칸을 사이에 두고 주어진다. 
0은 문제의 답이 틀린 경우이고, 1은 문제의 답이 맞는 경우이다. 

첫째 줄에 입력에서 주어진 채점 결과에 대하여 가산점을 고려한 총 점수를 출력한다. 
'''
a=input()
a=int(a)
n=input().strip().split(" ")
b=[]
for i in range(0,a):
    b.append(int(n[i]))
j=0
c=[]
for k in b:
    if k==0:
        j=0
        c.append(j)
    else:
        j=j+1
        c.append(j)
print(sum(c))
    


    


# In[ ]:




