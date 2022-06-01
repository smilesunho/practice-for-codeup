#!/usr/bin/env python
# coding: utf-8

# In[84]:
'''
두 주사위를 굴려 나오는 합 k 가 입력된다. 
합이 k가 되는 두 주사위의 눈이 출력된다. 
첫 번째 출력되는 수는 첫번째 주사위의 눈이고, 두 번째 출력되는 수는 두번째 주사위의 눈이다.
출력은 첫번째 주사위의 눈이 작은 수에서 큰 순서로 출력한다.
'''
n=int(input())
for i in range(1,7):
    for j in range(1,7):
        if i+j==n:
            print(i, j)

