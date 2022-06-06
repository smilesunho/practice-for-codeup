#!/usr/bin/env python
# coding: utf-8

# In[37]:


'''
희용이는 for문을 공부하다가 다음과 같은 프로그램을 생각해냈다.
a부터 b까지의 수 중에서 3의 배수는 더하고, 4의 배수는 빼는 프로그램을 만들어 보자.
만약 그 수가 3과 4의 공배수라면 더하거나 빼는 것을 생략한다.
예)
3 16
---> 3의 배수 = 3, 6, 9, 15 ( 12는 3과 4의 공배수이므로 제외 )
---> 4의 배수 = 4, 8, 16 ( 12는 3과 4의 공배수이므로 제외 )
==> 결과 = 5
'''
a,b=input().split(" ")
a=int(a)
b=int(b)
c=[]
for i in range(a,b+1):
    c.append(i)
i=0
z=[]
while i<=(b-a):
    if int(c[i])%3==0 and int(c[i])%4==0:
        pass
    elif int(c[i])%3==0:
        z.append(int(c[i]))
    elif int(c[i])%4==0:
        z.append((int(c[i]))*-1)
    else:
        pass
    i=i+1
print(sum(z))
        
   


