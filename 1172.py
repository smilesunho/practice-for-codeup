#!/usr/bin/env python
# coding: utf-8

# In[10]:


'''
세 수를 오름차순으로 정렬하려고 한다. (낮은 숫자 -> 높은 숫자)
예)
5 8 2   ====> 2 5 8    로 출력
'''
a=input().split(" ")
a=list(map(int,a))
for i in sorted(a):
    print(i, end=" ")

        


# In[ ]:




