#!/usr/bin/env python
# coding: utf-8

# In[25]:


'''
기상곡과 기상곡 사이에 AMOLED가 삽입되게 한다.
'''
a=int(input())
b=0
d=0
c=[]
while b<a:
    k=input()
    c.append(k)
    b=b+1

while d<=a-2:
    print(c[d])
    print("AMOLED")
    d=d+1
print(c[len(c)-1])

   



# In[ ]:


a=int(input())
b=0
d=0
c=[]
while b<a:
    k=input()
    c.append(k)
    b=b+1
if a%2==0:
    while d<=a-2:
        print(c[d])
        print("AMOLED")
        d=d+1
    print(c[len(c)-1])
else :
    while d<=a-2:
        print(c[d])
        print("AMOLED")
        d=d+1
    print(c[len(c)-1])
   

