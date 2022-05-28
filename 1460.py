#!/usr/bin/env python
# coding: utf-8

# In[5]:

'''
입력이 3인 경우 다음과 같이 출력한다.
1 2 3
4 5 6
7 8 9

입력이 n인 경우의 2차원 배열을 출력해보자.
'''



a=int(input())
for i in range(0,a):
    for k in range(1,a+1):
        print(a*i+k, end=' ')
    print()

