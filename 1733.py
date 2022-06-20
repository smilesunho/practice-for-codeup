#!/usr/bin/env python
# coding: utf-8

# In[50]:


'''
입력으로 IOI가 입력될 경우, 
IOI is the International Olympiad in Informatics.를 출력하는 프로그램을 작성하시오.
만약 IOI가 아닌 다른 글자가 들어오는 경우, I don't care.를 출력한다.
'''
a=input()
a=str(a)
if a=='IOI':
    print("IOI is the International Olympiad in Informatics.")
else:
    print("I don't care.")

