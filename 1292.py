#!/usr/bin/env python
# coding: utf-8

# In[8]:


'''
도둑의 DNA의 특징은 DNA의 모든 숫자의 합을 7로 나눈 나머지가 4라는 사실을 알았다.
다음 날 경찰이 도둑으로 의심되는 사람을 검거하여 그들의 DNA 샘플을 가져왔다.
DNA 샘플을 분석하여 이 자가 도둑인지 아닌지를 판단하여 만약 도둑이라면 “suspect”, 아니면 “citizen”을 출력하는 프로그램을 작성하시오.

 길이가 10자리로 구성된 10진수가 입력된다.
 프로그램의 조건에 따라 “suspect” 또는 “citizen”을 출력한다.
'''
a=input().strip()
b=[]
for i in range(0,10):
    b.append(int(a[i]))
c=sum(b)
if c%7==4:
    print('suspect')
else:
    print('citizen')


# In[ ]:




