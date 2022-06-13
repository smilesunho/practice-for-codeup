#!/usr/bin/env python
# coding: utf-8

# In[31]:


'''
세 정수값을 입력한다.(각 사람의 몸무게 값은 200 이하의 자연수이다.)
 몸무게가 가벼운 사람부터 무거운 사람의 순서로 출력한다.
'''
a=list(map(int,input().split(" ")))
a=sorted(a)
for i in a:
    print(i,sep=" ",end=' ')


# In[ ]:




