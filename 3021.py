#!/usr/bin/env python
# coding: utf-8

# In[22]:


'''
int는 32비트, long long 은 64비트라서 이 보다 더 큰 숫자는 저장할 수 없다.
아주 큰 숫자의 덧셈을 하려고 한다.
계산 결과를 출력하시오.
'''
sum_result = []
f = 0 
a=list(map(int,input()))
b=list(map(int,input()))
if len(a)<len(b):
    z=a
    a=b
    b=z

for i in range(len(b)) :
    n_sum = a.pop() + b.pop() + f
    if n_sum >= 10 : 
        sum_result.append(n_sum - 10)
        f = 1   
    else : 
        sum_result.append(n_sum)
        f = 0

for i in range(len(a)) : 
    if f == 1 : 
        n_sum = a.pop() + f  

    else : 
        f = 0
        break

    if n_sum >= 10 : 
        sum_result.append(n_sum - 10)
        f = 1

if f == 1 : sum_result.append(1)

sum_result.reverse()
a.extend(sum_result)

print("".join(list(map(str,a))))   


# In[ ]:




