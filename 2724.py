#!/usr/bin/env python
# coding: utf-8

# In[68]:


'''
자연수 N이 입력되었을 때,
이 N을 2개 이상의 연속된 자연수의 합으로 나타낼 수 있는지 
계산하는 프로그램을 작성하시오.
예를 들어, 21을 나타내는 방법은 1+2+3+4+5+6, 6+7+8, 10+11  
이렇게 3가지가 있다. 
'''
a=input()
a=int(a)
b=[]

if a==1:
    print(0)
else:
    for i in range(0,int(a/2+1)):
        k=0
        while k<=a:
            i=i+1
            k=k+i
            if (k)==a:
                b.append(k)    
    print(len(b))


# In[ ]:




