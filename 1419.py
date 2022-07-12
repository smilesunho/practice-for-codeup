#!/usr/bin/env python
# coding: utf-8

# In[8]:


'''
영어 문장이 입력된다.

그 문장에서 love가 몇 번 나오는지 출력하시오.

'''
a=input().strip().split(" ")
j=0
for i in a:
    i=str(i)
    if len(i)>=4:
        for k in range(0,len(i)):
            if i[k]=='l':
                if i[k+1]=="o":
                    if i[k+2]=="v":
                        if i[k+3]=="e":
                            j=j+1
print(j)
                        


# In[ ]:




