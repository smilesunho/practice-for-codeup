#!/usr/bin/env python
# coding: utf-8

# In[7]:
'''
사람 이름이 영어로 나열되면서 콤마(,)로 구분되어 있을 때, 약어를 자동으로 생성하는 프로그램을 만드시오.
사람 이름의 첫글자는 반드시 대문자로 입력된다.
예를 들어, Changwon,Science,High,School 이 입력되면 CSHS 를 출력한다.

'''
a=input().split(",")
for i in a:
    print(i[0],sep='',end='')

