#!/usr/bin/env python
# coding: utf-8

# In[77]:
'''
길이 n이 입력되면 길이가 n인 사각형을 출력하시오.
단, 사각형은 * 모양으로 채운다.
'''
n=int(input())
a=[["*" for j in range(n)] for i in range(n)]
for k in range(0,n):
    print('{}'.format(''.join(a[k])))
    


# In[ ]:




