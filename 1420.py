#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
첫째 줄에 n이 입력된다. ( 3 <= n <= 50 )
둘째 줄 부터 n+1행까지 친구의 이름과 점수가 공백으로 분리되어 입력된다. 이름은 영문
세 번째로 높은 학생의 이름을 출력한다.
'''
a=int(input())
k={}
i=0
while i<a:
    b,c=input().strip().split(" ")
    k[int(c)]=b
    i=i+1
u=k.keys()
u=list(u)
u=sorted(u)
print(k[u[-3]])


# In[ ]:




