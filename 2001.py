#!/usr/bin/env python
# coding: utf-8

# In[18]:


'''
입력은 5 행으로 이루어지며, 한 줄에 하나씩 양의 정수가 적혀있다.
1행의 정수는 첫 번째 파스타 가격이다.
2행의 정수는 두 번째 파스타 가격이다.
3행의 정수는 세 번째 파스타 가격이다.
4행의 정수는 첫 번째 생과일 쥬스 가격이다.
5행의 정수는 두 번째 생과일 쥬스의 가격이다.
(모든 파스타와 생과일 쥬스의 가격은 100 원이상 2000원 이하이다.)

어느 날의 파스타와 생과일 쥬스의 가격이 주어 졌을 때, 
그 날 세트 메뉴의 대금의 최소값을 구하는 프로그램을 작성하라.
'''
import numpy as np
a1=input()
a2=input()
a3=input()
b1=input()
b2=input()
a1=int(a1)
a2=int(a2)
a3=int(a3)
b1=int(b1)
b2=int(b2)
k=[a1,a2,a3]
j=[b1,b2]
d=[]
for i in k:
    for c in j:
        d.append((i+c)*1.1)
print("{:.1f}".format(np.min(d)))
        








            
    





        
        


# In[ ]:




