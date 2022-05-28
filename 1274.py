#!/usr/bin/env python
# coding: utf-8

# In[44]:
'''
입력으로 주어진 수가 소수이면 "prime"을 출력, 소수가 아니면 "not prime"을 출력한다.

'''

a=input()
a=int(a)
if a==2:
    print("prime")
#elif a==7453:
#    print("not prime")
else:    
    for i in range(2,a):
        if a%i==0:
            break
        else : 
            continue
    if a%i==0:
        print("not prime")
    else :
        print("prime")
            
            
    
  

