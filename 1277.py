#!/usr/bin/env python
# coding: utf-8

# In[4]:
'''
입력으로 N이 주어지고 그 다음줄에 N개의 데이터가 공백으로 구분되어 입력된다.(단, N>=1인 홀수)
첫번째, 중간, 마지막 데이터 값을 출력한다.
'''

a=int(input())
b=input().split()
c=(a//2)
print (b[0], b[c],b[a-1])

