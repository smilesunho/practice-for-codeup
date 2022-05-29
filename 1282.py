#!/usr/bin/env python
# coding: utf-8

# In[38]:
'''
n이 입력되면 k를 빼서 제곱수를 만들 수 있는 k를 구하고,
그 제곱수에 루트를 씌운 수(제곱근) t를 구하여라.
이 때 k는 여러가지가 될 수 있는데 가장 작은 k를 출력한다.
'''

n=int(input())
a=[]
for i in range(1,(n+1)):
    if i*i <=n:
        a.append(i*i)
    else :
        break 
w=int(max(a))
y=int((w**(1/2)))
print(n-w, y)
               


# In[ ]:




