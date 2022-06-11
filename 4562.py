#!/usr/bin/env python
# coding: utf-8

# In[6]:


'''
첫 째 줄에 A가, 둘째 줄에 B가, 셋째 줄에 C가 주어진다. A, B, C는 모두 100보다 같거나 크고, 1000보다 작은 자연수이다

첫째 줄에는 A×B×C의 결과에 0이 몇 번 쓰여졌는지를 출력한다. 마찬가지로 둘째 줄부터 열 번째 줄까지 A×B×C의 결과에 1부터 9까지의 숫자가 각각 몇 번 쓰여져 있는지 차례로 한 줄에 하나씩 출력한다.
'''
a=int(input())
b=int(input())
c=int(input())
d=a*b*c
e=str(d)
a0=[]
a1=[]
a2=[]
a3=[]
a4=[]
a5=[]
a6=[]
a7=[]
a8=[]
a9=[]
for i in range(0,len(e)):
    f=int(e[i])
    if f==0:
        a0.append(f)
    elif f==1:
        a1.append(f)
    elif f==2:
        a2.append(f)    
    elif f==3:
        a3.append(f)
    elif f==4:
        a4.append(f) 
    elif f==5:
        a5.append(f)
    elif f==6:
        a6.append(f)    
    elif f==7:
        a7.append(f)
    elif f==8:
        a8.append(f)
    elif f==9:
        a9.append(f)
    else:
        pass
print(len(a0))
print(len(a1))
print(len(a2))
print(len(a3))
print(len(a4))
print(len(a5))
print(len(a6))
print(len(a7))
print(len(a8))
print(len(a9))


# In[ ]:




