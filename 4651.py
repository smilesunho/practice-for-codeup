#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
첫째 줄부터 셋째 줄까지 한 줄에 하나씩 결과를 도는 A, 개는 B, 걸은 C, 윷은 D, 모는 E로 출력 한다.

'''
a=list(map(int,input().strip().split(" ")))
b=list(map(int,input().strip().split(" ")))
c=list(map(int,input().strip().split(" ")))
if sum(a)==4:
   print('E')
elif sum(a)==3:
   print('A')
elif sum(a)==2:
   print('B')
elif sum(a)==1:
   print('C')
elif sum(a)==0:
   print('D')
   
if sum(b)==4:
   print('E')
elif sum(b)==3:
   print('A')
elif sum(b)==2:
   print('B')
elif sum(b)==1:
   print('C')
elif sum(b)==0:
   print('D')    
   
if sum(c)==4:
   print('E')
elif sum(c)==3:
   print('A')
elif sum(c)==2:
   print('B')
elif sum(c)==1:
   print('C')
elif sum(c)==0:
   print('D')    


# In[ ]:




