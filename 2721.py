#!/usr/bin/env python
# coding: utf-8

# In[6]:


'''
영어 소문자로 구성된 단어 S1, S2, S3가 있을때,
S1의 마지막 문자가 S2의 첫 글자와 같고,
S2의 마지막 글자가 S3의 첫 글자와 같고,
S3의 마지막 글자가 S1의 첫 글자와 같으면 순환 문자열이라고 한다.
예를 들어 turtle error robot 인 경우 순환 문자열이다.
세 단어가 주어졌을 때 순환 문자열이면 good을 출력, 아니면 bad를 출력하시오.
영어 소문자로 구성된 단어 S1, S2, S3가 있을때,
S1의 마지막 문자가 S2의 첫 글자와 같고,
S2의 마지막 글자가 S3의 첫 글자와 같고,
S3의 마지막 글자가 S1의 첫 글자와 같으면 순환 문자열이라고 한다.
예를 들어 turtle error robot 인 경우 순환 문자열이다.
세 단어가 주어졌을 때 순환 문자열이면 good을 출력, 아니면 bad를 출력하시오.
'''
a=input()
b=input()
c=input()
a=str(a)
b=str(b)
c=str(c)

if a[0]==c[len(c)-1] and b[0]==a[len(a)-1] and c[0]==b[len(b)-1]:
    print('good')
else:
    print('bad')






# In[ ]:




