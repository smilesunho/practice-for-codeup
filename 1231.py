#!/usr/bin/env python
# coding: utf-8

# In[24]:


'''
연산식이 한줄로 입력된다.

연산식의 형식은 정수+정수 또는 정수-정수 또는 정수*정수 또는 정수/정수의 형태이다.
'''
import numpy as np
a=input()
if "+" in a:
    c,d=a.split("+")
    c=int(c)
    d=int(d)
    print(c+d)
elif "-" in a:
    c,d=a.split("-")
    c=int(c)
    d=int(d)
    print(c-d)
elif "*" in a:
    c,d=a.split("*")
    c=int(c)
    d=int(d)
    print(c*d)    
elif "/" in a:
    c,d=a.split("/")
    c=int(c)
    d=int(d)
    print("{:.2f}".format(np.round(c/d,2)))


# In[ ]:





# In[ ]:




