#!/usr/bin/env python
# coding: utf-8

# In[16]:


'''
a , b , c , d 가 차례대로 입력으로 주어진다.(자연수)
a / b  >  c / d  이면  > 를 출력,
a / b =  c / d  이면  = 를 출력,
a / b  <  c / d  이면 < 를 출력.
'''
a,b,c,d=map(int,input().split(" "))
if (a/b)>(c/d):
    print(">")
elif (a/b)==(c/d):
    print("=")
else:
    print("<")

        


# In[ ]:




