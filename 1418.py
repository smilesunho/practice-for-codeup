#!/usr/bin/env python
# coding: utf-8

# In[10]:


'''
어떤 문자열이 있을 때 문자 t의 위치를 모두 찾아 출력하시오.
공백이 없는 문자열이 한 줄 입력된다.(10글자 이하)

소문자 t의 위치를 공백으로 분리하여 모두 출력하시오.

'''
a=input()
a=str(a)
k=1
for i in a:
    if i=='t':
        print(k,end=" ")
    k=k+1
    





# In[ ]:




