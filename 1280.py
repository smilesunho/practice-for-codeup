#!/usr/bin/env python
# coding: utf-8

# In[19]:


'''
홀수는 더하고 짝수는 빼는 식을 보여준후 결과를 출력한다.
첫수가 양수일 경우에도 앞에 +를 붙여서 출력.
단 결과가 양수일 경우에는 +를 붙이지 않는다.
'''
a,b=map(int,input().strip().split(" "))
c=[]
for i in range(a,b+1):
    if i%2==0:
        c.append(i*-1)
    else:
        c.append(i)
for i in c:
    if i>0:
        print("+{}".format(i),end='',sep='')
    else:
        print(i,end='',sep='')
print('=',sum(c),sep='')    


# In[ ]:




