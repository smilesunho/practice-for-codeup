#!/usr/bin/env python
# coding: utf-8

# In[14]:


'''
첫 째 줄에 M이, 둘째 줄에 N이 주어진다. 
M과 N은 10000이하의 자연수이며 M은 N보다 같거나 작다.

M이상 N이하의 자연수 중 완전제곱수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최소값을 출력한다. 
단, M이상 N이하의 자연수 중 완전제곱수가 없을 경우는 첫째 줄에 -1을 출력한다.
'''
a=int(input())
b=int(input())
c=int(a**(1/2)-1)
k=[]
while c**2<=b:
    if c**2>=a:
        k.append(c**2)
        c=c+1
    else:
        c=c+1
if len(k)==0:
    print("-1")
else:
    print(sum(k))
    print(k[0])


# In[ ]:




