#!/usr/bin/env python
# coding: utf-8

# In[26]:


'''
그림과 같이 길이가 n인 철판을 구부려서 단면이 직사각형인 
ㄷ자 모양을 만들려고 한다.
이 ㄷ자 모양을 수직으로 자른 단면의 넓이 S를 최대로 하려면 
양 끝에서 얼마만큼 구부려야 하는지 계산하시오.
'''
a=input()
a=int(a)
b=a/4
if a%4==0:
    print(int(b))
else:
    c=a//4
    c=int(c)
    d=c*(a-2*c)
    e=(c+1)
    f=e*(a-2*e)
    if d==f:
        print(c)
    elif f>d:
        print(e)
    else:
        print(c)

    
    

