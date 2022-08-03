#!/usr/bin/env python
# coding: utf-8

# In[4]:


'''
재호는 이번 시험에 받은 성적이 궁금했다.

점수가 입력되면 등급을 출력하시오.

등급)

 90점 이상 : A

80점 이상 : B

70점 이상 : C

60점 이상 : D

60점 미만 : F
'''

a=input()
a=int(a)

if a>89:
    print('A')
elif a>79:
    print('B')
elif a>69:
    print('C')
elif a>59:
    print('D')
else:
    print('F')


# In[ ]:




