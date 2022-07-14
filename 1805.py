#!/usr/bin/env python
# coding: utf-8

# In[4]:


'''
첫째 줄에 입체기동장치의 갯수 n이 입력된다. (1 <= n <= 100)

둘째 줄부터 n+1째 줄까지 각 줄에 입체기동장치의 식별번호 a와 가스 보유량 b가 주어진다.

a는 중복 될 수 없지만 b는 중복될 수 있다. (1 <= a <= 100), (0 <= b <= 10,000)

첫째 줄부터 n번째 줄까지 각 줄에 식별번호를 
오름차순으로 정렬해 가스 보유량과 같이 출력한다.

'''
a=input()
a=int(a)
j={}
i=0
k=[]
while i < a: 
    b,c=input().strip().split(" ")
    b=int(b)
    c=int(c)
    k.append(b)
    j[b]=c
    i=i+1

i=0
k=sorted(k)
for i in k:
    print(i,j[i])


    





        
        


# In[ ]:




