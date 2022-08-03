#!/usr/bin/env python
# coding: utf-8

# In[6]:


'''
1. 치즈버거 : 400 칼로리
2. 야채버거 : 340 칼로리
3. 우유 : 170 칼로리
4. 계란말이 : 100 칼로리
5. 샐러드 : 70 칼로리
이 메뉴들 중 2가지 메뉴를 선택했을 때 칼로리 합을 계산하고, 그 칼로리 합이 500보다 크면 "angry", 500이하면 "no angry"를 출력하시오

메뉴의 번호가 차례대로 두개 주어진다. (정수)
'''

a,c=input().strip().split()
a=int(a)
c=int(c)
b={1:400,2:340,3:170,4:100,5:70}
k=b[a]+b[c]
if k>500:
    print('angry')
else:
    print('no angry')


# In[ ]:




